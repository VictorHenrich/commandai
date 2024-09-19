from dotenv import load_dotenv
import asyncio


async def main() -> None:
    from core.instances import AppInstances
    from services.ai import AiService
    from serializers.ai import (
        WitIntegrationResultSerializer,
        WitIntegrationParamsSerializer,
    )

    import controllers.event

    try:
        while True:
            voice_data: str = await AiService.async_capture_microphone_data()

            integration_data: WitIntegrationParamsSerializer = (
                WitIntegrationParamsSerializer(message=voice_data)
            )

            wit_integration: WitIntegrationResultSerializer = (
                await AiService.integrate_with_wit(integration_data)
            )

            AppInstances.event.emit(
                wit_integration.event_name, wit_integration.event_data
            )

    except InterruptedError:
        quit()


if __name__ == "__main__":
    load_dotenv()

    asyncio.run(main())
