from typing import Dict, Any

from core.instances import AppInstances
from services.volume import VolumeService
from utils.types import AppEventTypes
from serializers.volume import (
    VolumeDecreaseSerializer,
    VolumeIncreaseSerializer,
    VolumeMuteSerializer,
)


@AppInstances.event.on(AppEventTypes.Volume.INCREASE.value)
async def increase_volume(data: Dict[str, Any]):
    serializer: VolumeIncreaseSerializer = VolumeIncreaseSerializer(**data)

    await VolumeService.increase_volume(serializer)


@AppInstances.event.on(AppEventTypes.Volume.DECREASE.value)
async def decrease_volume(data: Dict[str, Any]):
    serializer: VolumeDecreaseSerializer = VolumeDecreaseSerializer(**data)

    await VolumeService.decrease_volume(serializer)


@AppInstances.event.on(AppEventTypes.Volume.MUTE.value)
async def mute():
    serializer: VolumeMuteSerializer = VolumeMuteSerializer(mute=1)

    await VolumeService.mute(serializer)


@AppInstances.event.on(AppEventTypes.Volume.UNMUTE.value)
async def unmute():
    serializer: VolumeMuteSerializer = VolumeMuteSerializer(mute=0)

    await VolumeService.mute(serializer)
