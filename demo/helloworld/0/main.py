#!/usr/bin/env python3
"""Hello World example."""
from __future__ import annotations  # Python < 3.10 compatiblity

from pydantic_settings import BaseSettings


class Inputs(BaseSettings):
    """GitHub Actions inputs."""

    input_name: str
    input_title: str = ""


def run() -> str:
    """Print greeting phrase."""
    inputs = Inputs()
    print(greeting := f"Hello {' '.join((inputs.input_title, inputs.input_name))}!")  # noqa: FLY002
    return greeting


if __name__ == "__main__":
    run()
