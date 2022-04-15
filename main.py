from pyrogram import Client
from pyrogram import filters

bot = Client(
   session_name="tanovercos",
    api_id=1442738,
    api_hash="9c95p7c9ce59853g818ba0b0e2486737",
    bot_token="5179626757:AAFgODzhEXbx-oHqWU_x2huZzWNYeS6iz5U"
)

@bot.on_message(filters.private & filters.command(['start']))
async def start(client, message):
    await message.reply_text(text="Hello welcome!", reply_to_message_id=message.message_id, parse_mode="markdown")

bot.run()
