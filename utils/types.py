from enum import Enum


class AppEventTypes:
    class Volume(Enum):
        INCREASE = "increase_volume"

        DECREASE = "decrease_volume"

        MUTE = "mute_volume"

        UNMUTE = "increase_volume"

    class Browser(Enum):
        pass

    @classmethod
    def get_event_by_name(cls, event_name: str) -> Enum:
        for value in vars(cls).values():
            if isinstance(value, type) and issubclass(value, Enum):
                try:
                    return value(event_name)

                except ValueError:
                    continue

        raise Exception(f"Event '{event_name}' not found!")