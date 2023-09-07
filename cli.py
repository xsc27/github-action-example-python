#!/usr/bin/env python3
"""Command Line Interface module."""
from __future__ import annotations  # Python < 3.10 compatiblity

import typer

import main

cli = typer.Typer()


@cli.command()
def run_cli(
    input_http_code: int = typer.Argument(envvar="INPUT_HTTP_CODE"),
    input_api_token: str = typer.Option("", envvar="INPUT_API_TOKEN"),
) -> None:
    """Get HTTP status code Cats."""
    main.run(main.Inputs.init(locals()))


if __name__ == "__main__":
    cli()
