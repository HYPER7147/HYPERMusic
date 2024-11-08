from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://envs.sh/jX1.jpg")
START_IMG = getenv("START_IMG", "⭕  https://envs.sh/jX5.mp4

by: @HGBOTZ ❤️‍🔥")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/FALLEN_SUPPORT")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/FALLEN_SUPPORT_BOT")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6528832488").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
