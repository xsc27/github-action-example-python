#!/usr/bin/env python3
from __future__ import annotations  # Python < 3.10 compatiblity

import json
import sys

from httpx import HTTPError, request
from pydantic import BaseSettings, SecretStr, ValidationError

URL = "https://httpcats.com/"


class Inputs(BaseSettings):
    # Define defaults at the APIs
    # i.e., action.yaml and the run_from_cli function
    input_status_code: int
    input_api_token: SecretStr


def get_cat(inputs: Inputs | None = None) -> dict[str, str | int]:
    try:
        inputs = inputs or Inputs()  # type: ignore
    except ValidationError as err:
        sys.exit(str(err))

    headers = {
        "content-type": "application/json",
        "X-API-Key": inputs.input_api_token.get_secret_value(),
    }
    resp = request("GET", f"{URL}/{inputs.input_status_code}.json", headers=headers)

    try:
        resp.raise_for_status()
    except HTTPError as err:
        sys.exit(str(err))

    data = resp.json()
    data.pop("image", None)

    return data


def print_json(data: dict[str, str | int]):
    print(json.dumps(data, indent=2))


if __name__ == "__main__":
    print_json(get_cat())
