from pyee import EventEmitter
from typer import Typer


class AppInstances:
    event: EventEmitter = EventEmitter()

    cli: Typer = Typer()
