from typing import Dict, Any
from speech_recognition import (
    Microphone,
    Recognizer,
    AudioData,
    UnknownValueError,
    RequestError,
)
import httpx
import logging
import asyncio

from utils.settings import WIT_BASE_URL, WIT_SECRET_KEY
from utils.serializers import WitIntegrationSerializer


class AiService:
    __recognizer: Recognizer = Recognizer()

    @classmethod
    def capture_microphone_data(cls) -> str:
        with Microphone() as source:
            try:
                logging.info("...Capturing Microphone Data...")

                cls.__recognizer.adjust_for_ambient_noise(source)

                audio_data: AudioData = cls.__recognizer.listen(source)

                return cls.__recognizer.recognize_google_cloud(
                    audio_data, language="pt-BR"
                )

            except UnknownValueError:
                raise Exception("Unable to understand the audio!")

            except RequestError:
                raise Exception("Failed to communicate with recognizer!")

    @classmethod
    async def async_capture_microphone_data(cls) -> str:
        return await asyncio.get_event_loop().run_in_executor(
            None, cls.capture_microphone_data
        )

    @staticmethod
    async def integrate_with_wit(message: str) -> WitIntegrationSerializer:
        wit_url: str = f"{WIT_BASE_URL}/message"

        query_params: Dict[str, Any] = {"q": message}

        async with httpx.AsyncClient(
            headers={"Authorization": f"Bearer {WIT_SECRET_KEY}"}
        ) as client:
            response: httpx.Response = await client.get(
                wit_url, params=query_params, timeout=10
            )

            response_data: Dict[str, Any] = response.json()

            return WitIntegrationSerializer(**response_data)
