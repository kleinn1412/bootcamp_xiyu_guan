import os
from pathlib import Path
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parent.parent


def load_env():
    load_dotenv(PROJECT_ROOT / ".env")


def get_key(name, default=None):
    return os.getenv(name, default)


load_env()

DATA_DIR = PROJECT_ROOT / "data"