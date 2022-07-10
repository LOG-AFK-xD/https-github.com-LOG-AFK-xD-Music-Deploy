""" inline section button """
import os
import sys
import random
import asyncio
from config import API_HASH, API_ID, BOT_TOKEN, SESSION_NAME, SESSION2

from pyrogram.types import (
  CallbackQuery,
  InlineKeyboardButton,
  InlineKeyboardMarkup,
  Message,
)
from config import GROUP_SUPPORT, UPDATES_CHANNEL

def stream_markup(user_id):
  buttons = [
    [
      InlineKeyboardButton(text="• Mᴇɴᴜ", callback_data=f'cbmenu | {user_id}'),
      InlineKeyboardButton(text="• Cʟᴏsᴇ", callback_data=f'cls'),
    ],
    [
      InlineKeyboardButton(text="✦ Sᴜᴩᴩᴏʀᴛ", url=f"https://t.me/UNIQUE_SOCIETY"),
      InlineKeyboardButton(text=" Uᴩᴅᴀᴛᴇꜱ ✦", url=f"https://t.me/ITzz_Official"),
    ],
  ]
  return buttons


def menu_markup(user_id):
  buttons = [
    [
      InlineKeyboardButton(text="⏹", callback_data=f'cbstop | {user_id}'),
      InlineKeyboardButton(text="⏸", callback_data=f'cbpause | {user_id}'),
      InlineKeyboardButton(text="▶️", callback_data=f'cbresume | {user_id}'),
    ],
    [
      InlineKeyboardButton(text="🔇", callback_data=f'cbmute | {user_id}'),
      InlineKeyboardButton(text="🔊", callback_data=f'cbunmute | {user_id}'),
    ],
    [
      InlineKeyboardButton(text="🗑 Close", callback_data='cls'),
    ]
  ]
  return buttons


close_mark = InlineKeyboardMarkup(
  [
    [
      InlineKeyboardButton(
        "🗑 Close", callback_data="cls"
      )
    ]
  ]
)


back_mark = InlineKeyboardMarkup(
  [
    [
      InlineKeyboardButton(
        "🔙 Go Back", callback_data="cbmenu"
      )
    ]
  ]
)
