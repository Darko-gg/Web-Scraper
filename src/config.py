from pathlib import Path

# Project root = folder above /src
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Data folders
DATA_DIR = PROJECT_ROOT / "data"
INPUT_DIR = DATA_DIR / "input"
OUTPUT_DIR = DATA_DIR / "output"

# Default output settings
DEFAULT_OUTPUT_FORMAT = "json"
DEFAULT_OUTPUT_FILENAME = "results.json"