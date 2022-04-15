from pyrogram import Client
from pyrogram.types import (InlineQueryResultArticle, InputTextMessageContent,
                            InlineKeyboardMarkup, InlineKeyboardButton)
from pyrogram import filters
import logging
logging.basicConfig(filename='mylog.log', level=logging.ERROR)

bot = Client(
   session_name="tanovercos",
    api_id=14027438,
    api_hash="9c9527c9c3e59853818ba0b0e2486737",
    bot_token="5181588402:AAEx5GzBQNZ3PY-h5usaRFa-55fKzaSxNwY"
)

@bot.on_inline_query()
def answer(client, inline_query):
    inline_query.answer(
        results=[
            InlineQueryResultArticle(
                title="creator",
                input_message_content=InputTextMessageContent(
                    "salam baraye payam dadan be man ruye in click kon"
                ),
                url="https://t.me/tan_over_cos",
                description="id man",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton(
                            "click me",
                            url="https://t.me/tan_over_cos"
                        )]
                    ]
                )
            ),
          
        ],
        cache_time=1
    )
  
@bot.on_message(filters.private & filters.command(['start']))
async def start(client, message):
    await message.reply_text(text="your start", reply_to_message_id=message.message_id, parse_mode="markdown")

bot.run()  # Automatically start() and idle()
