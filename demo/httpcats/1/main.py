#!/usr/bin/env python3
"""HTTP Status Cats client."""
from __future__ import annotations  # Python < 3.10 compatiblity

import argparse
import json
import os
from typing import Any, Sequence

from httpx import ConnectError, HTTPError, request

URL = "https://httpcats.com"


def fetch_data(input_http_code: str, input_api_token: str) -> Any:
    """Return HTTP Status Cats data."""
    headers = {
        "content-type": "application/json",
        "X-API-Key": input_api_token,
    }
    resp = request("GET", f"{URL}/{input_http_code}.json", headers=headers)
    resp.raise_for_status()
    return resp.json()


def get_cli_parser() -> argparse.ArgumentParser:
    """Return CLI argument parser."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input_http_code",
        type=int,
        default=os.getenv("INPUT_HTTP_CODE"),
        help="HTTP status code (env var: INPUT_HTTP_CODE)",
    )
    parser.add_argument(
        "--input_api_token",
        default=os.getenv("INPUT_API_TOKEN"),
        help="API token (env var: INPUT_API_TOKEN)",
    )

    return parser


def run(args: Sequence[Any] | None = None) -> Any:
    """Print HTTP Status Cats data."""
    parser = get_cli_parser()
    inputs = vars(parser.parse_args(args))
    if not all(inputs.values()):
        parser.print_help()
        raise SystemExit(1)

    try:
        data = fetch_data(**inputs)
    except (ConnectError, HTTPError) as err:
        msg = f"{err.__class__.__name__}: {err!s}"
        raise SystemExit(msg) from err
    print(json.dumps(data, indent=2))

    return data


if __name__ == "__main__":
    run()
