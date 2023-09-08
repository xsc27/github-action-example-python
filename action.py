#!/usr/bin/env python3
"""Shim for GitHub action."""
from __future__ import annotations  # Python < 3.10 compatiblity

import io
import json
import logging
import os
import sys
from pathlib import Path

from typer.testing import CliRunner

from cli import cli


def write(out_env: str, text: str) -> None:
    """Write to GitHub Action files.

    Args:
        out_env (str): Name of the enviroment variable
        text (str): Text to write
    """
    with Path(f).open("at") if (f := os.getenv(out_env)) else io.StringIO() as fid:
        fid.write(f"\n{text}\n")
        if isinstance(fid, io.StringIO):
            logging.info("%s:\n%s", out_env, fid.getvalue())


def run() -> None:
    """Run main GitHub Action business logic."""
    result = CliRunner().invoke(app=cli, args=sys.argv[1:])

    if result.exit_code:
        raise SystemExit(result.output.strip())

    try:
        data = json.loads(result.output)
    except json.decoder.JSONDecodeError as err:
        # handle `--help`
        print(result.output)
        raise SystemExit(f"{err.__class__.__name__}: {err}" if result.exit_code else 0) from err

    title = f"{data['status_code']} - {data['title']}"
    write("GITHUB_STEP_SUMMARY", f"## {title}\n![{title}]({data['url']}.jpg)")
    write("GITHUB_OUTPUT", f"description={data['title']}\nimage={data['url']}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    run()
