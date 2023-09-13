#!/usr/bin/env python3
"""Hello World example."""
from __future__ import annotations  # Python < 3.10 compatiblity

import argparse
import os
from typing import Sequence


def get_greeting(input_name: str) -> str:
    """Return greeting phrase."""
    return f"Hello {input_name}!"


def get_cli_parser() -> argparse.ArgumentParser:
    """Return CLI argument parser."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input_name",
        default=os.getenv("INPUT_NAME"),
        help="Who to greet (env var: INPUT_NAME)",
    )

    return parser


def run(args: Sequence[str] | None = None) -> str:
    """Print greeting phrase."""
    parser = get_cli_parser()
    inputs = vars(parser.parse_args(args))
    if not all(inputs.values()):
        parser.print_help()
        raise SystemExit(1)

    print(greeting := get_greeting(**inputs))

    return greeting


if __name__ == "__main__":
    run()
