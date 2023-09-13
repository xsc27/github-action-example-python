#!/usr/bin/env python3
"""Hello World example."""
from __future__ import annotations  # Python < 3.10 compatiblity

import os
import sys


def get_greeting(input_name: str = "World") -> str:
    """Return greeting phrase."""
    return f"Hello {input_name}!"


def run(input_name: str | None = None) -> str:
    """Print greeting phrase."""
    if not (name := input_name or " ".join(sys.argv[1:]) or os.getenv("INPUT_NAME")):
        msg = "ERROR: An argument or environment variable INPUT_NAME is required!"
        raise SystemExit(msg)
    print(greeting := get_greeting(name))

    return greeting


if __name__ == "__main__":
    run()
