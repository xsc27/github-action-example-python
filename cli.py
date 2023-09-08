#!/usr/bin/env python3
"""Command Line Interface module."""

from __future__ import annotations  # Python < 3.10 compatiblity

import contextlib
from importlib.metadata import PackageNotFoundError, version

import typer
from pydantic import ValidationError

import main

cli = typer.Typer()


def version_callback(flag: bool) -> bool:
    """Print version number."""
    if not flag:
        return flag
    ver = "0.0.0"
    with contextlib.suppress(PackageNotFoundError):
        ver = version("github-action-example-python")
    print(ver)
    raise SystemExit


@cli.command()
def run_cli(
    input_http_code: int = typer.Argument(envvar="INPUT_HTTP_CODE"),
    input_api_token: str = typer.Option("", envvar="INPUT_API_TOKEN"),
    version: bool = typer.Option(
        False,
        "--version",
        callback=version_callback,
        help="Print version.",
    ),
) -> None:
    """Get HTTP status code Cats."""
    try:
        main.run(locals())
    except ValidationError as err:
        raise SystemExit(str(err)) from err


if __name__ == "__main__":
    cli()
