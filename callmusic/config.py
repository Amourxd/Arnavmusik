from os import getenv

from dotenv import load_dotenv

load_dotenv()

admins = {}

SESSION_NAME = getenv("SESSION_NAME")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
BOT_USERNAME = getenv("BOT_USERNAME", "RessoMusikbot")
BOT_TOKEN = getenv("BOT_TOKEN")
API_ID = int(getenv("API_ID", "26864680"))
API_HASH = getenv("API_HASH", "7dab04a9f63156e9e9911c55dd87d56e")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "ilexworld")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "op_arnav_singh")
OWNER_ID = list(map(int, getenv("OWNER_ID", "5482561033").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5482561033").split()))
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "1300")) 
BOT_NAME = getenv("BOT_NAME", "ʀɛֆֆօ ʍʊֆɨƈ ɮօȶ")
YOUTUBE_IMG_URL = getenv(
    "YOUTUBE_IMG_URL", "https://telegra.ph/file/1dd11896b4c843ffa7906.jpg"
)
