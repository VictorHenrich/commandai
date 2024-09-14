from speech_recognition import (
    Microphone,
    Recognizer,
    AudioData,
    UnknownValueError,
    RequestError,
)
import logging


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
