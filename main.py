from pyrogram import Client as Bot
from pytgcalls import idle
from callsmusic import run
from config import API_ID, API_HASH, BOT_TOKEN

bot = Bot(
    ":memory:",
    API_ID=13953815
    API_HASH=7810709783
    bot_token=7810709783:AAGs2TQyXtHVQyL6U-LBYHEB466mdROBDRs
    plugins=dict(root="handlers")
)

bot.start()
run()
idle()
