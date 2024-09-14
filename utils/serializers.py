from pydantic import BaseModel, field_validator


class BaseVolumeControlSerializer(BaseModel):
    volume: float

    component: str = ""


class VolumeIncreaseSerializer(BaseVolumeControlSerializer):
    @field_validator("volume")
    def validate_volume(cls, value: float) -> float:
        if value < 0 or value == 0:
            raise ValueError("Invalid value for increasing volume: {value}")

        return value


class VolumeDecreaseSerializer(BaseVolumeControlSerializer):
    @field_validator("volume")
    def validate_volume(cls, value: float) -> float:
        if value > 0 or value == 0:
            raise ValueError("Invalid value for decreasing volume: {value}")

        return value


class VolumeMuteSerializer(BaseModel):
    mute: int

    component: str = ""

    @field_validator("mute", mode="before")
    def set_mute_as_integer(cls, value: bool) -> int:
        return 1 if value else 0
