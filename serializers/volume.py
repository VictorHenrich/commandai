from typing import Union, Dict, Any
from pydantic import BaseModel, field_validator, model_validator

from utils.settings import MAX_VALUE_NIRCMD_VOLUME
from utils.common import AppCommon


class VolumeAdjustSerializer(BaseModel):
    volume: Union[int, str]

    component: str = ""

    @model_validator(mode="before")
    def validate_model(cls, value: Dict[str, Any]):
        if (isinstance(value, dict) and value.get("volume")) or hasattr(
            value, "volume"
        ):
            return value

        return {
            "volume": value["volume_value"],
            "component": value.get("volume_component", ""),
        }
    
    @field_validator("volume", mode="after")
    def validate_volume(cls, value: Union[int, str]) -> int:
        try:
            number: int = int(AppCommon.keep_only_numbers(str(value)))

        except ValueError:
            raise ValueError(f"The Value passed is invalid for numeric values.")

        else:
            if type(value) is str and "%" in value:
                number = int((number / 100) * MAX_VALUE_NIRCMD_VOLUME)

            return number


class VolumeMuteSerializer(BaseModel):
    mute: int

    component: str = ""

    @field_validator("mute", mode="before")
    def set_mute_as_integer(cls, value: Union[bool, int]) -> int:
        if not isinstance(value, (bool, int)):
            raise ValueError("Invalid value to mute/unmute volume.")

        return 1 if value else 0
