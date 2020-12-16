import json
import logging
from typing import Any


def set_debug(log: logging.Logger, debug: bool) -> None:
    if debug is True:
        log.setLevel(logging.DEBUG)
    else:
        log.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")
    handler.setFormatter(formatter)
    log.addHandler(handler)


def write_json(what: Any, filename: str) -> None:
    with open(filename, "w") as fd:
        json.dump(what, fd, indent=2)
