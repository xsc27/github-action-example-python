#!/usr/bin/env python3
"""Main business logic."""
from __future__ import annotations  # Python < 3.10 compatiblity

import json
from functools import singledispatch
from typing import Any

from httpx import ConnectError, HTTPError, request
from pydantic import BaseSettings, Extra, SecretStr, ValidationError, validator

URL = "https://httpcats.com"
HTTP_CODE_RANGE = (100, 599)


class Inputs(BaseSettings):
    """GitHub Action inputs."""

    input_http_code: int
    input_api_token: SecretStr

    class Config:
        """Configure base model."""

        extra = Extra.ignore

    @validator("input_http_code")
    def check_status_code_range(cls, http_code: int) -> int:  # noqa: ANN101, N805
        """Check if the status code is in a valid range."""
        if http_code < HTTP_CODE_RANGE[0] or http_code > HTTP_CODE_RANGE[1]:
            msg = "Valid HTTP status codes are from 100 to 599."
            raise ValueError(msg)
        return http_code


@singledispatch
def run(inputs: dict[str, Any] | Inputs) -> dict[str, str | int]:  # noqa: ARG001
    """Get data from HTTP Status Cats API."""
    return run(Inputs())


@run.register(dict)
def _(inputs: dict[str, Any]) -> dict[str, str | int]:
    return run(Inputs(**inputs))


@run.register
def _(inputs: Inputs) -> dict[str, str | int]:
    headers = {
        "content-type": "application/json",
        "X-API-Key": inputs.input_api_token.get_secret_value(),
    }
    try:
        resp = request("GET", f"{URL}/{inputs.input_http_code}.json", headers=headers)
    except ConnectError as err:
        msg = f"{err.__class__.__name__}: {err!s}"
        raise SystemExit(msg) from err

    try:
        resp.raise_for_status()
    except HTTPError as err:
        raise SystemExit(str(err)) from err

    data: dict[str, str | int] = resp.json()
    data.pop("image", None)

    print(json.dumps(data, indent=2))

    return data


if __name__ == "__main__":
    try:
        run({})
    except ValidationError as err:
        raise SystemExit(str(err)) from err
