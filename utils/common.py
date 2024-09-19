import subprocess
import asyncio
import re


class AppCommon:
    @staticmethod
    def execute_command(command: str) -> subprocess.CompletedProcess[bytes]:
        return subprocess.run(command, shell=True)

    @classmethod
    async def async_execute_command(
        cls, command: str
    ) -> subprocess.CompletedProcess[bytes]:
        event_loop: asyncio.AbstractEventLoop = asyncio.get_event_loop()

        return await event_loop.run_in_executor(None, cls.execute_command, command)

    @staticmethod
    def keep_only_numbers(string: str) -> str:
        return re.sub(r"\D", "", string)
