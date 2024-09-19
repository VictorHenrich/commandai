from serializers.volume import (
    VolumeAdjustSerializer,
    VolumeMuteSerializer,
)
from utils.settings import (
    NIRCMD_PATH,
    COMMAND_ADJUST_VOLUME,
    COMMAND_MUTE_VOLUME,
)
from utils.common import AppCommon


class VolumeService:
    @staticmethod
    async def adjust_volume(data: VolumeAdjustSerializer) -> None:
        command: str = f"{NIRCMD_PATH} {COMMAND_ADJUST_VOLUME}".format(
            data.volume, data.component
        )

        await AppCommon.async_execute_command(command)

    @staticmethod
    async def mute(data: VolumeMuteSerializer):
        command: str = f"{NIRCMD_PATH} {COMMAND_MUTE_VOLUME}".format(
            data.mute, data.component
        )

        await AppCommon.async_execute_command(command)
