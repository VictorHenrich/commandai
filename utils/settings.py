from pathlib import Path
import os


NIRCMD_PATH: Path = Path(__file__).parent / ".." / "binaries" / "nircmd.exe"

MAX_VALUE_NIRCMD_VOLUME: int = int(os.environ.get("MAX_VALUE_NIRCMD_VOLUME", "65535"))

WIT_BASE_URL: str = os.environ.get("WIT_BASE_URL", "https://api.wit.ai")
WIT_SECRET_KEY: str = os.environ.get(
    "WIT_SECRET_KEY", "6VOF7XPGB2MGV7UNFIJLULACRACK2T57"
)

COMMAND_INCREASE_VOLUME: str = os.environ.get(
    "COMMAND_INCREASE_VOLUME", "setsysvolume {}"
)

COMMAND_DECREASE_VOLUME: str = os.environ.get(
    "COMMAND_INCREASE_VOLUME", "setsysvolume {}"
)

COMMAND_MUTE_VOLUME: str = os.environ.get("COMMAND_INCREASE_VOLUME", "mutesysvolume {}")
