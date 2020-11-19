import logging
from functools import wraps

import click
import yaml

log = logging.getLogger("kafkaadmin")


def logging_option(func):
    @click.option("-d", "--debug", default=False, is_flag=True, help="enable debug output")
    @click.pass_context
    @wraps(func)
    def wrapper(ctx, *args, **kwargs):
        debug = kwargs.pop("debug")
        ctx.debug = debug
        if debug is True:
            log.setLevel(logging.DEBUG)
        else:
            log.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")
        handler.setFormatter(formatter)
        log.addHandler(handler)
        ctx.log = log

        return func(*args, **kwargs)

    return wrapper


def config_option(func):
    @click.option(
        "-c", "--config", type=click.File("r"), default="./config.yml", help="specify custom path for config file"
    )
    @click.pass_context
    @wraps(func)
    def wrapper(ctx, *args, **kwargs):
        ctx.config = yaml.safe_load(kwargs.pop("config"))

        return func(*args, **kwargs)

    return wrapper
