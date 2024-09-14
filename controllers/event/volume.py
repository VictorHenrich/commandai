from typing import Dict, Any

from core.instances import AppInstances
from services.volume import VolumeService
from utils.serializers import (
    VolumeDecreaseSerializer,
    VolumeIncreaseSerializer,
    VolumeMuteSerializer
)


@AppInstances.event.on("increase_volume")
def increase_volume(data: Dict[str, Any]):
    serializer: VolumeIncreaseSerializer = VolumeIncreaseSerializer(**data)

    VolumeService.increase_volume(serializer)

@AppInstances.event.on("decrease_volume")
def decrease_volume(data: Dict[str, Any]):
    serializer: VolumeDecreaseSerializer = VolumeDecreaseSerializer(**data)

    VolumeService.decrease_volume(serializer)

@AppInstances.event.on("mute")
def mute():
    serializer: VolumeMuteSerializer = VolumeMuteSerializer(mute=1)

    VolumeService.mute(serializer)

@AppInstances.event.on("unmute")
def unmute():
    serializer: VolumeMuteSerializer = VolumeMuteSerializer(mute=0)

    VolumeService.mute(serializer)