#!/usr/bin/env python3
"""HTTP Status Cats client."""
from __future__ import annotations  # Python < 3.10 compatiblity

import argparse
import json
from typing import Any, Sequence

from httpx import ConnectError, HTTPError, request
from pydantic import SecretStr, ValidationError
from pydantic_settings import BaseSettings

URL = "https://httpcats.com"


class Inputs(BaseSettings):
    """Application inputs."""

    input_http_code: int
    input_api_token: SecretStr


def fetch_data(inputs: Inputs) -> Any:
    """Return HTTP Status Cats data."""
    headers = {
        "content-type": "application/json",
        "X-API-Key": inputs.input_api_token.get_secret_value(),
    }
    resp = request("GET", f"{URL}/{inputs.input_http_code}.json", headers=headers)
    resp.raise_for_status()
    return resp.json()


def get_cli_parser() -> argparse.ArgumentParser:
    """Return CLI argument parser."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input_http_code",
        type=int,
        help="HTTP status code (env var: INPUT_HTTP_CODE)",
    )
    parser.add_argument(
        "--input_api_token",
        help="API token (env var: INPUT_API_TOKEN)",
    )

    return parser


def run(args: Sequence[Any] | None = None) -> Any:
    """Print HTTP Status Cats data."""
    inputs = vars(get_cli_parser().parse_args(args))
    inputs = dict(filter(lambda x: x[1] is not None, inputs.items()))

    try:
        data = fetch_data(Inputs(**inputs))
    except (ConnectError, HTTPError, ValidationError) as err:
        msg = f"{err.__class__.__name__}: {err!s}"
        raise SystemExit(msg) from err
    print(json.dumps(data, indent=2))

    return data


if __name__ == "__main__":
    run()
