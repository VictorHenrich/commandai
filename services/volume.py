import subprocess

from utils.serializers import VolumeDecreaseSerializer, VolumeMuteSerializer, VolumeIncreaseSerializer
from utils.settings import (
    NIRCMD_PATH,
    COMMAND_DECREASE_VOLUME,
    COMMAND_INCREASE_VOLUME,
    COMMAND_MUTE_VOLUME
)



class VolumeService:
    @staticmethod
    def increase_volume(data: VolumeIncreaseSerializer):
        command: str = f"{NIRCMD_PATH} {COMMAND_INCREASE_VOLUME}".format(data.volume, data.component)

        subprocess.run(command, shell=True)

    @staticmethod
    def decrease_volume(data: VolumeDecreaseSerializer):
        command: str = f"{NIRCMD_PATH} {COMMAND_DECREASE_VOLUME}".format(data.volume, data.component)

        subprocess.run(command, shell=True)

    @staticmethod
    def mute(data: VolumeMuteSerializer):
        command: str = f"{NIRCMD_PATH} {COMMAND_MUTE_VOLUME}".format(data.mute, data.component)

        subprocess.run(command, shell=True)