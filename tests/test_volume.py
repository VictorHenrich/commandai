from typing import Any
from unittest import IsolatedAsyncioTestCase
from unittest.mock import Mock

from services.volume import VolumeService
from serializers.volume import (
    VolumeAdjustSerializer,
    VolumeMuteSerializer,
)


class VolumeServiceTestCase(IsolatedAsyncioTestCase):
    async def test_increase_volume_with_success(self) -> None:
        increase_volume_data: Mock = Mock(volume=8000, component="")

        await VolumeService.adjust_volume(increase_volume_data)

    async def test_increase_volume_with_validation_success(self) -> None:
        increase_volume_data: VolumeAdjustSerializer = VolumeAdjustSerializer(
            volume="80%"
        )

        await VolumeService.adjust_volume(increase_volume_data)

    async def test_increase_volume_with_validation_error(self) -> None:
        error_value: str = "VALOR INVÁLIDO"

        error_message: str = (
            r"Value error, The Value passed is invalid for numeric values."
        )

        with self.assertRaisesRegex(
            expected_exception=ValueError, expected_regex=error_message
        ):
            increase_volume_data: VolumeAdjustSerializer = VolumeAdjustSerializer(
                volume=error_value
            )

            await VolumeService.adjust_volume(increase_volume_data)

    async def test_mute_volume_with_success(self) -> None:
        increase_volume_data: Mock = Mock(mute=1, component="")

        await VolumeService.mute(increase_volume_data)

    async def test_mute_volume_with_validation_success(self) -> None:
        increase_volume_data: VolumeMuteSerializer = VolumeMuteSerializer(mute=True)

        await VolumeService.mute(increase_volume_data)

    async def test_mute_volume_with_validation_error(self) -> None:
        error_value: Any = "VALOR INVÁLIDO"

        error_message: str = r"Invalid value to mute/unmute volume."

        with self.assertRaisesRegex(
            expected_exception=ValueError, expected_regex=error_message
        ):
            increase_volume_data: VolumeMuteSerializer = VolumeMuteSerializer(
                mute=error_value
            )

            await VolumeService.mute(increase_volume_data)

    async def test_unmute_volume_with_success(self) -> None:
        increase_volume_data: Mock = Mock(mute=0, component="")

        await VolumeService.mute(increase_volume_data)

    async def test_unmute_volume_with_validation_success(self) -> None:
        increase_volume_data: VolumeMuteSerializer = VolumeMuteSerializer(mute=False)

        await VolumeService.mute(increase_volume_data)

    async def test_unmute_volume_with_validation_error(self) -> None:
        error_value: Any = "VALOR INVÁLIDO"

        error_message: str = r"Invalid value to mute/unmute volume."

        with self.assertRaisesRegex(
            expected_exception=ValueError, expected_regex=error_message
        ):
            increase_volume_data: VolumeMuteSerializer = VolumeMuteSerializer(
                mute=error_value
            )

            await VolumeService.mute(increase_volume_data)
