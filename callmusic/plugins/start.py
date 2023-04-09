from datetime import datetime

from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from callmusic import BOT_NAME, BOT_USERNAME
from callmusic import bot as Kanna
from callmusic.config import GROUP_SUPPORT, UPDATES_CHANNEL

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("ᴡᴇᴇᴋs", 60 * 60 * 24 * 7),
    ("ᴅᴀʏ", 60**2 * 24),
    ("ʜᴏᴜʀ", 60**2),
    ("ᴍɪɴ", 60),
    ("sᴇᴄ", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Kanna.on_message(filters.command(["start", "help"]) & ~filters.group)
async def start(_, message: Message):
    await message.reply_text(
        f"""**ɦɛʟʟօ {BOT_NAME}✨ ȶɦɨֆ ǟɖʋǟռƈɛ 🌠 ʋɨɖɛօ 🥀 ȶɛʟɛɢʀǟʍ ʍʊֆɨƈ 🎻 ǟռɖ ʋɨɖɛօ 🎥 ɮօȶ ʀʊռ օռ քʀɨʋǟȶɛ 🥀 ʋքֆ 🌐ǟʀռǟʋ ֆɛʀʋɛʀ 🛰️ ʄɛɛʟ ❤️ ɦɨɢɦ զʊǟʟɨȶʏ ʍʊֆɨƈ 🎧 ɨռ ʋօɨƈɛ ƈɦǟȶ ɮօȶ 😎🤟
🛰️ քօաɛʀɛɖ ɮʏ: [ɨʟɛӼ ֆɛʀʋɛʀ](https://t.me/Arnavserver) 💞...**""",
     reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ 𝐀𝐃𝐃 𝐌𝐄 ❱ ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
                ],
                [
                    InlineKeyboardButton(
                        "🛰 ʊքɖǟȶɛֆ", url=f"https://t.me/op_arnav_singh"),

                    InlineKeyboardButton(
                        "ֆʊքքօʀȶ 💌", url=f"https://t.me/ilexworld"),
                ],
                [
                    InlineKeyboardButton(
                        text="🥀 ❰ 𝗖𝐮𝐭𝐞 𝐎𝐰𝐧𝐞𝐫シ︎𝐱𝐃 ❱ ✨", url=f"https://t.me/cute_arnavsingh")
                ]
           ]
        ),
      disable_web_page_preview=True,
     )


@Kanna.on_message(filters.command(["repo", "kanna"]))
async def help(client: Kanna, message: Message):
    await message.reply_text(
        text=f"**𝗥𝐄𝐬𝐬𝐎𝗠𝘂𝘀𝗶𝗰𝗫 ❣️ 𝗶𝘀 𝗮𝗻 𝗽𝗼𝘄𝗲𝗿𝗳𝘂𝗹 🌐 𝗺𝘂𝘀𝗶𝗰 𝘀𝗼𝘂𝗿𝗰𝗲 🚬 𝗠𝗮𝗸𝗲 𝘂𝗿 𝗳𝗿𝗼𝗸 ⚜️ 𝗮𝗻𝗱 𝗴𝗶𝘃𝗲 𝗼𝗻𝗲 ⭐ 𝗳𝗼𝗿 𝗼𝘂𝗿 𝗵𝗮𝗿𝗱 𝘄𝗼𝗿𝗸 🥀**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⭐ʀᴇᴘᴏ✨", url=f"https://te.legra.ph/file/a615d91c0ef7caaa70fdd.mp4"
                    )
                ]
            ]
        ),
    )

@Kanna.on_message(filters.command(["kana"]) & filters.group)
async def start(client: Kanna, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        f"""✔ **ʙᴏᴛ ɪs ʀᴜɴɴɪɴɢ**\n<b>☣ **ᴜᴘᴛɪᴍᴇ:**</b> `{uptime}`""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝐎𝐰𝐧𝐞𝐫-𝐱𝐃", url=f"https://t.me/cute_arnavsingh"
                    ),
                    InlineKeyboardButton(
                        "𝐒𝐮𝐩𝐩𝐨𝐫𝐭 📩", url=f"https://t.me/Arnavserver"
                    ),
                ]
            ]
        ),
    )
