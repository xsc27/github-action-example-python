#!/usr/bin/env python3
"""GitHub Action module."""
from __future__ import annotations  # Python < 3.10 compatiblity

import io
import logging
import os
from pathlib import Path

import main


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
    data = main.run()
    title = f"{data['status_code']} - {data['title']}"
    write("GITHUB_STEP_SUMMARY", f"## {title}\n![{title}]({data['url']}.jpg)")
    write("GITHUB_OUTPUT", f"description={data['title']}\nimage={data['url']}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    run()
