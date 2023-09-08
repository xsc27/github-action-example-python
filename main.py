#!/usr/bin/env python3
"""Main business logic."""
from __future__ import annotations  # Python < 3.10 compatiblity

import json
import sys
from typing import TYPE_CHECKING, Any

from httpx import ConnectError, HTTPError, request
from pydantic import BaseSettings, SecretStr, ValidationError, validator

if TYPE_CHECKING:  # Mypy compatiblity
    from typing_extensions import Self

URL = "https://httpcats.com"
HTTP_CODE_RANGE = (100, 599)


class Inputs(BaseSettings):
    """GitHub Action inputs."""

    input_http_code: int
    input_api_token: SecretStr

    @validator("input_http_code")
    def check_status_code_range(cls: Self, val: int) -> int:  # noqa: N805
        """Check if the status code is in a valid range.

        Args:
            val (int): HTTP status code

        Raises:
            ValueError: HTTP status code is out of range.

        Returns:
            int: A valid HTTP status code
        """
        if val < HTTP_CODE_RANGE[0] or val > HTTP_CODE_RANGE[1]:
            msg = "Valid HTTP status codes are from 100 to 599."
            raise ValueError(msg)
        return val

    @classmethod
    def init(cls: type[Self], kwargs: dict[str, Any] | None = None) -> Self:
        """Instantiate object.

        Args:
            kwargs (dict[str, str  |  int] | None, optional): Values for object. Defaults to None.

        Returns:
            Self: Inputs object.
        """
        kwargs = kwargs or {}
        try:
            return cls(**kwargs)
        except ValidationError as err:
            sys.exit(str(err))


def run(inputs: Inputs | None = None) -> dict[str, str | int]:
    """Get data from HTTP Status Cats API."""
    inputs = inputs or Inputs.init()

    headers = {
        "content-type": "application/json",
        "X-API-Key": inputs.input_api_token.get_secret_value(),
    }
    try:
        resp = request("GET", f"{URL}/{inputs.input_http_code}.json", headers=headers)
    except ConnectError as err:
        sys.exit(str(err))

    try:
        resp.raise_for_status()
    except HTTPError as err:
        sys.exit(str(err))

    data: dict[str, str | int] = resp.json()
    data.pop("image", None)

    print(json.dumps(data, indent=2))

    return data


if __name__ == "__main__":
    run()
