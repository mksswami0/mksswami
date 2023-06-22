from telethon import TelegramClient
import logging
import time


api_id = "1125689"
api_hash = "4772d1792ed194020a8fb06a91ffb8fa"
bot_token = "5412301522:AAEjXLV97Lx8CHHrGIjFDFyPSdyFWBdZNlI"

bot = TelegramClient(("Mksswamibot"), api_id, api_hash).start(bot_token = bot_token)