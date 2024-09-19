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
        intent: str = values["intents"][0]

        entities: Dict[str, Any] = values["entities"]

        cls.event_name = AppEventTypes.get_event_by_name(intent)

        cls.event_data = {
            prop.split(":")[0]: entitie_data.get("body")
            for prop, entitie_data in entities.items()
        }

        return values
