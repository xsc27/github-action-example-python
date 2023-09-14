#!/usr/bin/env python3
"""HTTP Status Cats client."""
from __future__ import annotations  # Python < 3.10 compatiblity

import json
from typing import Any, Optional

import typer
from httpx import ConnectError, HTTPError, request
from pydantic import SecretStr, ValidationError, field_validator
from pydantic_settings import BaseSettings

URL = "https://httpcats.com"
HTTP_CODE_RANGE = (100, 599)


class Inputs(BaseSettings):
    """Application inputs."""

    input_http_code: int
    input_api_token: SecretStr

    @field_validator("input_http_code")
    def check_status_code_range(cls, val: int) -> int:  # noqa: ANN101, N805
        """Check if the status code is in a valid range."""
        if val < HTTP_CODE_RANGE[0] or val > HTTP_CODE_RANGE[1]:
            msg = f"Valid HTTP status code range is {list(HTTP_CODE_RANGE)}."
            raise ValueError(msg)
        return val


def fetch_data(inputs: Inputs) -> Any:
    """Return HTTP Status Cats data."""
    headers = {
        "content-type": "application/json",
        "X-API-Key": inputs.input_api_token.get_secret_value(),
    }
    resp = request("GET", f"{URL}/{inputs.input_http_code}.json", headers=headers)
    resp.raise_for_status()
    return resp.json()


def run(input_http_code: Optional[int] = None, input_api_token: Optional[str] = None) -> Any:  # noqa: UP007
    """Print HTTP Status Cats data."""
    inputs = dict(filter(lambda x: x[1] is not None, locals().items()))
    try:
        data = fetch_data(Inputs(**inputs))
    except (ConnectError, HTTPError, ValidationError) as err:
        msg = f"{err.__class__.__name__}: {err!s}"
        raise SystemExit(msg) from err

    print(json.dumps(data, indent=2))

    return data


if __name__ == "__main__":
    typer.run(run)
