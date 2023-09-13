#!/usr/bin/env python3
"""Hello World example."""
from __future__ import annotations  # Python < 3.10 compatiblity

import argparse
from typing import Sequence

from pydantic_settings import BaseSettings


class Inputs(BaseSettings):
    """Application inputs."""

    input_name: str


def get_greeting(inputs: Inputs) -> str:
    """Return greeting phrase."""
    return f"Hello {inputs.input_name}!"


def get_cli_parser() -> argparse.ArgumentParser:
    """Return CLI argument parser."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input_name",
        help="Who to greet (env var: INPUT_NAME)",
    )

    return parser


def run(args: Sequence[str] | None = None) -> str:
    """Print greeting phrase."""
    args_ns = get_cli_parser().parse_args(args)
    inputs = {k: v for k, v in vars(args_ns).items() if v}
    print(greeting := get_greeting(Inputs(**inputs)))

    return greeting


if __name__ == "__main__":
    run()
