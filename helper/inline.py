from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from youtubesearchpython import VideosSearch

from callmusic.config import GROUP_SUPPORT as Kanna


def ytsearch(query):
    try:
        search = VideosSearch(query, limit=1).result()
        data = search["result"][0]
        songname = data["title"]
        url = data["link"]
        duration = data["duration"]
        thumbnail = f"https://i.ytimg.com/vi/{data['id']}/hqdefault.jpg"
        videoid = data["id"]
        return [songname, url, duration, thumbnail, videoid]
    except Exception as e:
        print(e)
        return 0


def audio_markup(user_id):
  buttons = [
    [
      InlineKeyboardButton(text="😎 ƈʊȶɛօառɛʀ 🥀", url=f"https://t.me/cute_arnavsingh")
    ],
    [
      InlineKeyboardButton(text="🛰️ ʊքɖǟȶɛֆ", url=f"https://t.me/op_arnav_singh"),
      InlineKeyboardButton(text="ɨռʄօʀʍ 📩", url=f"https://t.me/ilexworld")
    ],
    [
      InlineKeyboardButton(text="💌 ʄɛɛʟɨռɢ'ֆ 😎", url=f"https://t.me/aboutarnav")
    ], 
  ]
  return buttons

def stream_markup(user_id, dlurl):
  buttons = [
    [
      InlineKeyboardButton(text="😎 ƈʊȶɛօառɛʀ 🥀", url=f"https://t.me/cute_arnavsingh")
    ],
    [
      InlineKeyboardButton(text="🛰️ ʊքɖǟȶɛֆ", url=f"https://t.me/op_arnav_singh"),
      InlineKeyboardButton(text="ɨռʄօʀʍ 📩", url=f"https://t.me/ilexworld")
    ],
    [
      InlineKeyboardButton(text="💌 ʄɛɛʟɨռɢ'ֆ 😎", url=f"https://t.me/aboutarnav")
    ], 
  ]
  return buttons

close_mark = InlineKeyboardMarkup(
  [
    [
      InlineKeyboardButton(
        "• ƈʟօֆɛ •", callback_data="cls"
      )
    ]
  ]
)
