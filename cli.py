#!/usr/bin/env python3
"""Command Line Interface module."""
from __future__ import annotations  # Python < 3.10 compatiblity

import typer

import main


def _run(status_code: int, api_token: str = ""):
    """Get HTTP status code Cats."""
    kwargs = {f"input_{k}": v for k, v in locals().items()}
    main.run(main.Inputs.init(kwargs))


def run():
    """Run CLI."""
    typer.run(_run)


if __name__ == "__main__":
    run()
