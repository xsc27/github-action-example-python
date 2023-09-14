#!/usr/bin/env python3
"""GitHub actions shim."""
from __future__ import annotations  # Python < 3.10 compatiblity

import os
from pathlib import Path

import main


def run() -> None:
    """Set GitHub Actions specific settings."""
    with Path(os.getenv("GITHUB_OUTPUT", "github_output.txt")).open(mode="at", encoding="utf-8") as fid:
        fid.write(f"\ngreeting={main.run()}\n")


if __name__ == "__main__":
    run()
