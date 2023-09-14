#!/usr/bin/env python3
"""GitHub actions shim."""
from __future__ import annotations  # Python < 3.10 compatiblity

import json
import os
from pathlib import Path

import main


def run() -> None:
    """Set GitHub Actions specific settings."""
    with Path(os.getenv("GITHUB_OUTPUT", "github_output.txt")).open(mode="at", encoding="utf-8") as fid:
        data = main.run()
        fid.write(f"\ntitle={data['title']}\nimage={data['url']}.jpg\ndata={json.dumps(data)}\n")


if __name__ == "__main__":
    run()
