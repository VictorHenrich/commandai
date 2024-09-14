from pathlib import Path
import os


NIRCMD_PATH: Path = Path(__file__) / '..' / 'binaries' / 'nircmd'

COMMAND_INCREASE_VOLUME: str = os.environ.get('COMMAND_INCREASE_VOLUME', 'setsysvolume {}')

COMMAND_DECREASE_VOLUME: str = os.environ.get('COMMAND_INCREASE_VOLUME', 'setsysvolume {}')

COMMAND_MUTE_VOLUME: str = os.environ.get('COMMAND_INCREASE_VOLUME', 'mutesysvolume {}')