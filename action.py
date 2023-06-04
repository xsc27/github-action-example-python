#!/usr/bin/env python3
from __future__ import annotations  # Python < 3.10 compatiblity

import io
import logging
import os
from pathlib import Path

from main import get_cat, print_json


def to_md(data: dict[str, str | int]) -> str:
    name = f"{data['status_code']} - {data['title']}"
    return f"## {name}\n![{name}]({data['url']}.jpg)"


def write(out_env: str, text: str):
    with Path(f).open("at") if (f := os.getenv(out_env)) else io.StringIO() as fid:
        fid.write(f"\n{text}\n")
        if isinstance(fid, io.StringIO):
            logging.info("%s:\n%s", out_env, fid.getvalue())


def run():
    data = get_cat()
    print_json(data)
    write("GITHUB_STEP_SUMMARY", to_md(data))
    write("GITHUB_OUTPUT", f"description={data['title']}\nimage={data['url']}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    run()
