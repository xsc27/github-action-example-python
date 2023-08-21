#!/usr/bin/env python3
"""Main business logic."""
from __future__ import annotations  # Python < 3.10 compatiblity

import json
import sys
from typing import Any, Self, Type

from httpx import HTTPError, request
from pydantic import BaseSettings, SecretStr, ValidationError, validator

URL = "https://httpcats.com"
HTTP_STATUS_CODE_RANGE = (100, 599)


class Inputs(BaseSettings):
    """GitHub Action inputs."""

    # Define defaults at the APIs
    # i.e., action.yaml and the run_from_cli function
    input_status_code: int
    input_api_token: SecretStr

    @validator("input_status_code")
    def check_status_code_range(cls: Self, val: int) -> int:  # noqa: N805
        """Check if the status code is in a valid range.

        Args:
            val (int): HTTP status code

        Raises:
            ValueError: HTTP status code is out of range.

        Returns:
            int: A valid HTTP status code
        """
        if val < HTTP_STATUS_CODE_RANGE[0] or val > HTTP_STATUS_CODE_RANGE[1]:
            msg = "Valid HTTP status codes are from 100 to 599."
            raise ValueError(msg)
        return val

    @classmethod
    def init(cls: Type[Self], kwargs: dict[str, Any] | None = None) -> Self:  # noqa: UP006
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
    resp = request("GET", f"{URL}/{inputs.input_status_code}.json", headers=headers)

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
