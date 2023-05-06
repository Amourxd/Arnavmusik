from pyrogram import Client
from pytgcalls import PyTgCalls, idle

from callmusic.config import API_HASH, API_ID, BOT_TOKEN, OWNER_ID, SESSION_NAME
from callmusic.plugins import ALL_PLUGINS

bot = Client(
    "callmusic",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
)

kanna = Client(
      api_id=API_ID,
      api_hash=API_HASH,
      session_name=SESSION_NAME,
)

user = PyTgCalls(
    kanna,
    cache_duration=100,
    overload_quiet_mode=True,
)

call_py = PyTgCalls(kanna, overload_quiet_mode=True)

OWNER_NAME = "UrssKanna"
F_OWNER = OWNER_ID[0]

with Client("callmusic", API_ID, API_HASH, bot_token=BOT_TOKEN) as app:
    x = app.get_me()
    BOT_ID = x.id
    BOT_NAME = x.first_name + (x.last_name or "")
    BOT_USERNAME = x.username
    BOT_MENTION = x.mention
    BOT_DC_ID = x.dc_id
with kanna as ass:
    getass = ass.get_me()
    ASSISTANT_USERNAME = getass.username
