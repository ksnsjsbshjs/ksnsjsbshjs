from pyrogram import Client
from pyrogram import filters

bot = Client(
   session_name="tanovercos",
    api_id=14027438,
    api_hash="9c9527c9c3e59853818ba0b0e2486737",
    bot_token="2104213051:AAHgzWPAN8SnZZbUhVQtHWp5ECpHgJ9upws"
)

@bot.on_message(filters.private & filters.command(['start']))
async def start(client, message):
    await message.reply_text(text="Hello welcome!", reply_to_message_id=message.message_id, parse_mode="markdown")

bot.run()
