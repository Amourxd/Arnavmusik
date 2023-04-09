import asyncio
from pyrogram import filters
from pyrogram.errors import FloodWait
from pyrogram.types import Message
from callmusic.config import OWNER_ID
from callmusic import bot, kanna

@bot.on_message(filters.command("broadcast") & filters.user(OWNER_ID))
async def broadcast(_, message: Message):
    brep = await message.reply_text("sᴛᴀʀᴛᴇᴅ ᴀssɪsᴛᴀɴᴛ ʙʀᴏᴀᴅᴄᴀsᴛ...")
    if message.reply_to_message:
        x = message.reply_to_message.message_id
        y = message.chat.id
    else:
        if len(message.command) < 2:
            return await message.reply_text(
                "ᴇxᴀᴍᴘʟᴇ:\n\n/broadcast [ᴍᴇssᴀɢᴇ] ᴏʀ [ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ]"
            )
        query = message.text.split(None, 1)[1]
    sent = 0
    chats = []
    async for dialog in await bot.get_dialogs():
        chats.append(int(dialog.chat.id))
    for i in chats:
        try:
            await bot.forward_messages(
                chat_id=i, from_chat_id=y, message_ids=x
            ) if message.reply_to_message else await bot.send_message(chat_id=i, text=query)
            sent += 1
        except FloodWait as e:
            flood_time = int(e.x)
            if flood_time > 200:
                continue
            await asyncio.sleep(flood_time)
        except Exception:
            continue
    try:
        await brep.edit_text(f"ʙʀᴏᴀᴅᴄᴀsᴛᴇᴅ ᴍᴇssᴀɢᴇ ɪɴ {sent} ᴄʜᴀᴛs.")
    except:
        await message.reply_text(f"ʙʀᴏᴀᴅᴄᴀsᴛᴇᴅ ᴍᴇssᴀɢᴇ ɪɴ {sent} ᴄʜᴀᴛs.")
