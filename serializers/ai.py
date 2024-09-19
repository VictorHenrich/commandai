from typing import Dict, Any
from pydantic import BaseModel, model_validator
from enum import Enum

from utils.types import AppEventTypes


class WitIntegrationParamsSerializer(BaseModel):
    message: str


class WitIntegrationResultSerializer(BaseModel):
    event_name: Enum

    event_data: Dict[str, Any]

    @model_validator(mode="before")
    def handle_wit_integration_data(cls, values: Any) -> Any:
        try:
            intent: str = values["intents"][0]["name"]

            entities: Dict[str, Any] = values["entities"]

            event_name: Enum = AppEventTypes.get_event_by_name(intent)

            event_data: Dict[str, Any] = {
                prop.split(":")[0]: entitie_data[0].get("body")
                for prop, entitie_data in entities.items()
            }

            return {"event_name": event_name, "event_data": event_data}

        except Exception as error:
            raise ValueError(
                f"Unable to validate data integration with wit: {values}\n"
                + f"Exception: {error}"
            )
