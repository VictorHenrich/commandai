from typing import Type
from enum import Enum


class AppEventTypes:
    class Volume(Enum):
        __EVENT_NAME__ = "volume"

        INCREASE = "increase_volume"

        DECREASE = "decrease_volume"

        MUTE = "mute_volume"

        UNMUTE = "increase_volume"

    class Browser(Enum):
        __EVENT_NAME__ = "browser"

    @classmethod
    def get_event_by_name(cls, event_name: str) -> Type[Enum]:
        for value in vars(cls).values():
            if (
                isinstance(value, type)
                and hasattr(value, "__EVENT_NAME__")
                and value.__EVENT_NAME___.lower() == event_name.lower()
            ):
                return value

        raise Exception(f"Event '{event_name}' not found!")
