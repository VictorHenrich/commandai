from pyee.asyncio import AsyncIOEventEmitter
from typer import Typer


class AppInstances:
    event: AsyncIOEventEmitter = AsyncIOEventEmitter()

    cli: Typer = Typer()
