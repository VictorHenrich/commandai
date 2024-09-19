from unittest import IsolatedAsyncioTestCase
from unittest.mock import Mock, patch
from pathlib import Path
import speech_recognition as sr

from services.ai import AiService
from utils.types import AppEventTypes
from serializers.ai import (
    WitIntegrationParamsSerializer,
    WitIntegrationResultSerializer,
)
from tests.common import RESOURCES_PATH


AUDIO_PATH: Path = RESOURCES_PATH / "volume_increase_command.wav"


class AiServiceTestCase(IsolatedAsyncioTestCase):
    async def test_integrate_with_wit_with_success(self) -> None:
        wit_integration_data: Mock = Mock(message="Eu quero aumentar o volume para 30%")

        wit_integration_response: WitIntegrationResultSerializer = (
            await AiService.integrate_with_wit(wit_integration_data)
        )

        self.assertEqual(
            wit_integration_response.event_name, AppEventTypes.Volume.INCREASE
        )

    @patch("services.ai.Microphone", new=lambda *_: sr.AudioFile(str(AUDIO_PATH)))
    async def test_capture_microphone_data_with_success(self) -> None:
        expected_message: str = r"aumentar volume para 80%"

        message: str = await AiService.async_capture_microphone_data()

        self.assertIsNotNone(message)

        self.assertTrue(message)

        self.assertRegex(message, expected_message)
