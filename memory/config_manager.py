import os
import sys
from pathlib import Path
from dotenv import load_dotenv, set_key


def get_base_dir() -> Path:
    if getattr(sys, "frozen", False):
        return Path(sys.executable).parent
    return Path(__file__).resolve().parent.parent


BASE_DIR = get_base_dir()
ENV_FILE = BASE_DIR / ".env"

# Load environment variables from .env if it exists
if ENV_FILE.exists():
    load_dotenv(ENV_FILE)


def save_api_keys(gemini_api_key: str) -> None:
    gemini_api_key = gemini_api_key.strip()
    
    # Save to .env (Preferred)
    try:
        if not ENV_FILE.exists():
            ENV_FILE.touch()
        set_key(str(ENV_FILE), "GEMINI_API_KEY", gemini_api_key)
        # Update current process environment
        os.environ["GEMINI_API_KEY"] = gemini_api_key
        print(f"[Config] ✅ Saved API key to .env")
    except Exception as e:
        print(f"⚠️ Failed to save to .env: {e}")


def get_gemini_key() -> str | None:
    # Check Environment variable (direct or from .env)
    key = os.getenv("GEMINI_API_KEY")
    if key and len(key.strip()) > 15:
        return key.strip()
    return None


def is_configured() -> bool:
    key = get_gemini_key()
    return bool(key and len(key) > 15)