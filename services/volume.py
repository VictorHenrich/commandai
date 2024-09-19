from serializers.volume import (
    VolumeDecreaseSerializer,
    VolumeMuteSerializer,
    VolumeIncreaseSerializer,
)
from utils.settings import (
    NIRCMD_PATH,
    COMMAND_DECREASE_VOLUME,
    COMMAND_INCREASE_VOLUME,
    COMMAND_MUTE_VOLUME,
)
from utils.common import AppCommon


class VolumeService:
    @staticmethod
    async def increase_volume(data: VolumeIncreaseSerializer):
        command: str = f"{NIRCMD_PATH} {COMMAND_INCREASE_VOLUME}".format(
            data.volume, data.component
        )

        await AppCommon.async_execute_command(command)

    @staticmethod
    async def decrease_volume(data: VolumeDecreaseSerializer):
        command: str = f"{NIRCMD_PATH} {COMMAND_DECREASE_VOLUME}".format(
            data.volume, data.component
        )

        await AppCommon.async_execute_command(command)

    @staticmethod
    async def mute(data: VolumeMuteSerializer):
        command: str = f"{NIRCMD_PATH} {COMMAND_MUTE_VOLUME}".format(
            data.mute, data.component
        )

        await AppCommon.async_execute_command(command)
