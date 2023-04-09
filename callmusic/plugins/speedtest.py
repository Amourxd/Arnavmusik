import asyncio
import speedtest

from pyrogram import filters
from callmusic import bot as Kanna
from pyrogram.types import Message
from helper.filters import command
from helper.decorators import sudo_users_only


def testspeed(m):
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        m = m.edit("🔱")
        test.download()
        m = m.edit("😝")
        test.upload()
        test.results.share()
        result = test.results.dict()
        m = m.edit("🥱")
    except Exception as e:
        return m.edit(e)
    return result


@Kanna.on_message(command("speedtest"))
@sudo_users_only
async def speedtest_function(Kanna: Kanna, message: Message):
    m = await message.reply_text("❤")
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, testspeed, m)
    output = f"""**sᴘᴇᴇᴅᴛᴇsᴛ ʀᴇsᴜʟᴛs**
    
<u>**ᴄʟɪᴇɴᴛ:**</u>
**__ɪsᴘ:__** {result['client']['isp']}
**__ᴄᴏᴜɴᴛʀʏ:__** {result['client']['country']}
  
<u>**ᴇsᴘᴏʀᴛs sᴇʀᴠᴇʀ:**</u>
**__ɴᴀᴍᴇ:__** {result['server']['name']}
**__ᴄᴏᴜɴᴛʀʏ:__** {result['server']['country']}, {result['server']['cc']}
**__sᴘᴏɴsᴏʀ:__** {result['server']['sponsor']}
**__ʟᴀᴛᴇɴᴄʏ:__** {result['server']['latency']}  
**__ᴘɪɴɢ:__** {result['ping']}"""
    msg = await Kanna.send_photo(
        chat_id=message.chat.id, 
        photo=result["share"], 
        caption=output
    )
    await m.delete()
