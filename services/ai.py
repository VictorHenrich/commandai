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
import os
import logging

from utils.settings import WIT_BASE_URL, WIT_SECRET_KEY, GOOGLE_API_KEY
from serializers.ai import (
    WitIntegrationResultSerializer,
    WitIntegrationParamsSerializer,
)


class AiService:
    __recognizer: Recognizer = Recognizer()

    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = GOOGLE_API_KEY

    @classmethod
    def __recognize_with_whisper(cls, audio_data: AudioData) -> str:
        return cls.__recognizer.recognize_whisper(audio_data, language="pt")

    @classmethod
    def __recognize_with_google(cls, audio_data: AudioData) -> str:
        return cls.__recognizer.recognize_google_cloud(audio_data, language="pt-BR")

    @classmethod
    def __capture_audio_data(cls, source: Microphone) -> AudioData:
        cls.__recognizer.adjust_for_ambient_noise(source)

        return cls.__recognizer.listen(source)

    @classmethod
    def capture_microphone_data(cls) -> str:
        with Microphone() as source:
            try:
                logging.info("...Capturing Microphone Data...")

                audio_data: AudioData = cls.__capture_audio_data(source)

                message: str = cls.__recognize_with_whisper(audio_data)

                logging.info(f"Speech to Text Message: {message}")

                return message

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
    async def integrate_with_wit(
        data: WitIntegrationParamsSerializer,
    ) -> WitIntegrationResultSerializer:
        wit_url: str = f"{WIT_BASE_URL}/message"

        query_params: Dict[str, Any] = {"q": data.message}

        async with httpx.AsyncClient(
            headers={"Authorization": f"Bearer {WIT_SECRET_KEY}"}
        ) as client:
            response: httpx.Response = await client.get(
                wit_url, params=query_params, timeout=10
            )

            response_data: Dict[str, Any] = response.json()

            logging.info(f"Wit Integration Response: {response_data}")

            return WitIntegrationResultSerializer(**response_data)
