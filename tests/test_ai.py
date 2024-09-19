from unittest import IsolatedAsyncioTestCase
from unittest.mock import Mock, AsyncMock, MagicMock, patch
from pathlib import Path
import speech_recognition as sr

from services.ai import AiService
from serializers.ai import (
    WitIntegrationParamsSerializer,
    WitIntegrationResultSerializer,
)
from utils.types import AppEventTypes
from utils.settings import WIT_BASE_URL
from tests.common import RESOURCES_PATH


AUDIO_PATH: Path = RESOURCES_PATH / "volume_adjust_command.wav"


class AiServiceTestCase(IsolatedAsyncioTestCase):
    async def test_integrate_with_wit_with_success(self) -> None:
        wit_integration_data: Mock = Mock(message="aumentar o volume para 30%")

        wit_integration_response: WitIntegrationResultSerializer = (
            await AiService.integrate_with_wit(wit_integration_data)
        )

        self.assertEqual(
            wit_integration_response.event_name, AppEventTypes.Volume.ADJUST
        )

    async def test_integrate_with_wit_with_validation_success(self) -> None:
        wit_integration_data: WitIntegrationParamsSerializer = (
            WitIntegrationParamsSerializer(message="ajustar o volume para 30%")
        )

        wit_integration_response: WitIntegrationResultSerializer = (
            await AiService.integrate_with_wit(wit_integration_data)
        )

        self.assertEqual(
            wit_integration_response.event_name, AppEventTypes.Volume.ADJUST
        )

    async def test_integrate_with_wit_with_validation_error(self) -> None:
        wit_integration_data: WitIntegrationParamsSerializer = (
            WitIntegrationParamsSerializer(message="Eu quero voar")
        )

        with self.assertRaisesRegex(
            expected_exception=ValueError,
            expected_regex=r"Unable to validate data integration with wit",
        ):
            await AiService.integrate_with_wit(wit_integration_data)

    @patch("services.ai.httpx.AsyncClient")
    async def test_integrate_with_wit_with_integration_error(
        self, mock_httpx_client: MagicMock
    ) -> None:
        response_status_code: int = 500

        response_representation: str = f"<Response status='{response_status_code}'/>"

        message_error: str = (
            "Integration with wit failed!\n" + f"Response: {response_representation}"
        )

        mock_async_client: AsyncMock = AsyncMock(name="MockAsyncClient")

        mock_response: Mock = MagicMock(
            status_code=response_status_code, content=b"teste"
        )

        mock_response.__repr__ = lambda *_: response_representation

        mock_response.__str__ = lambda *_: response_representation

        mock_async_client.get.return_value = mock_response

        mock_httpx_client.return_value = mock_httpx_client

        mock_httpx_client.__aenter__.return_value = mock_async_client

        mock_httpx_client.__aexit__.return_value = None

        wit_integration_data: WitIntegrationParamsSerializer = (
            WitIntegrationParamsSerializer(message="")
        )

        with self.assertRaisesRegex(
            expected_exception=Exception, expected_regex=rf"{message_error}"
        ):
            await AiService.integrate_with_wit(wit_integration_data)

        mock_httpx_client.__aenter__.assert_called_once_with()

        mock_httpx_client.__aexit__.assert_called_once()

        mock_async_client.get.assert_called_once_with(
            f"{WIT_BASE_URL}/message", params={"q": ""}, timeout=10
        )

    @patch("services.ai.Microphone", new=lambda *_: sr.AudioFile(str(AUDIO_PATH)))
    async def test_capture_microphone_data_with_success(self) -> None:
        expected_message: str = r"aumentar volume para 80%"

        message: str = await AiService.async_capture_microphone_data()

        self.assertIsNotNone(message)

        self.assertTrue(message)

        self.assertRegex(message, expected_message)
