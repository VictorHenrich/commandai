from dotenv import load_dotenv
import asyncio


async def main() -> None:
    from core.instances import AppInstances
    from services.ai import AiService
    from utils.serializers import WitIntegrationSerializer

    import controllers.event

    try:
        while True:
            voice_data: str = await AiService.async_capture_microphone_data()

            wit_integration: WitIntegrationSerializer = (
                await AiService.integrate_with_wit(voice_data)
            )

            AppInstances.event.emit(
                wit_integration.event_name, wit_integration.event_data
            )

    except InterruptedError:
        quit()


if __name__ == "__main__":
    load_dotenv()

    asyncio.run(main())
