from typing import Dict, Any

from core.instances import AppInstances
from services.volume import VolumeService
from utils.types import AppEventTypes
from serializers.volume import (
    VolumeAdjustSerializer,
    VolumeMuteSerializer,
)


@AppInstances.event.on(AppEventTypes.Volume.ADJUST.value)
async def increase_volume(data: Dict[str, Any]):
    serializer: VolumeAdjustSerializer = VolumeAdjustSerializer(**data)

    await VolumeService.adjust_volume(serializer)


@AppInstances.event.on(AppEventTypes.Volume.MUTE.value)
async def mute():
    serializer: VolumeMuteSerializer = VolumeMuteSerializer(mute=1)

    await VolumeService.mute(serializer)


@AppInstances.event.on(AppEventTypes.Volume.UNMUTE.value)
async def unmute():
    serializer: VolumeMuteSerializer = VolumeMuteSerializer(mute=0)

    await VolumeService.mute(serializer)
