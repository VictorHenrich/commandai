from typing import Dict, Any, Union
from pydantic import BaseModel, field_validator, model_validator

from utils.settings import MAX_VALUE_NIRCMD_VOLUME
from utils.common import AppCommon


class BaseVolumeControlSerializer(BaseModel):
    volume: Union[int, str]

    component: str = ""


class VolumeIncreaseSerializer(BaseVolumeControlSerializer):
    @field_validator("volume")
    def validate_volume(cls, value: Union[int, str]) -> int:
        try:
            number: int = int(AppCommon.keep_only_numbers(str(value)))

        except ValueError:
            raise ValueError(f"The Value passed is invalid for numeric values.")

        else:
            if type(value) is str and "%" in value:
                number = int((number / 100) * MAX_VALUE_NIRCMD_VOLUME)

            if number < 0:
                number *= -1

            return number


class VolumeDecreaseSerializer(BaseVolumeControlSerializer):
    @field_validator("volume")
    def validate_volume(cls, value: Union[int, str]) -> int:
        try:
            number: int = int(AppCommon.keep_only_numbers(str(value)))

        except ValueError:
            raise ValueError(f"The Value passed is invalid for numeric values.")

        else:
            if type(value) is str and "%" in value:
                number = int((number / 100) * MAX_VALUE_NIRCMD_VOLUME)

            if number > 0:
                number *= -1

            return number


class VolumeMuteSerializer(BaseModel):
    mute: int

    component: str = ""

    @field_validator("mute", mode="before")
    def set_mute_as_integer(cls, value: Union[bool, int]) -> int:
        if not isinstance(value, (bool, int)):
            raise ValueError("Invalid value to mute/unmute volume.")

        return 1 if value else 0


class WitIntegrationParamsSerializer(BaseModel):
    message: str


class WitIntegrationResultSerializer(BaseModel):
    event_name: str

    event_data: Dict[str, Any]

    @model_validator(mode="before")
    def handle_wit_integration_data(cls, values: Any) -> Any:
        return values
