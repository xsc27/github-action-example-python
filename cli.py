#!/usr/bin/env python3
from __future__ import annotations  # Python < 3.10 compatiblity

import sys

import typer
from pydantic import ValidationError

from main import Inputs, get_cat, print_json


def run(status_code: int, api_token: str = ""):
    kwargs = {f"inputs_{k}": v for k, v in locals().items() if v}

    try:
        inputs = Inputs(**kwargs)
    except ValidationError as err:
        sys.exit(str(err))

    print_json(get_cat(inputs))


if __name__ == "__main__":
    typer.run(run)
