from typing import Dict, Any

from core.instances import AppInstances
from services.volume import VolumeService
from utils.serializers import (
    VolumeDecreaseSerializer,
    VolumeIncreaseSerializer,
    VolumeMuteSerializer,
)


@AppInstances.event.on("increase_volume")
async def increase_volume(data: Dict[str, Any]):
    serializer: VolumeIncreaseSerializer = VolumeIncreaseSerializer(**data)

    await VolumeService.increase_volume(serializer)


@AppInstances.event.on("decrease_volume")
async def decrease_volume(data: Dict[str, Any]):
    serializer: VolumeDecreaseSerializer = VolumeDecreaseSerializer(**data)

    await VolumeService.decrease_volume(serializer)


@AppInstances.event.on("mute_volume")
async def mute():
    serializer: VolumeMuteSerializer = VolumeMuteSerializer(mute=1)

    await VolumeService.mute(serializer)


@AppInstances.event.on("unmute_volume")
async def unmute():
    serializer: VolumeMuteSerializer = VolumeMuteSerializer(mute=0)

    await VolumeService.mute(serializer)
