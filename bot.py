'''
© All rights reserved by Mrvishal2k2

Kangers dont f*ckin kang this !!!
Should have to give credits 😏 else f***off 
This is only for personal use Dont use this for ur bot channel business 😂
Thanks to Mahesh Malekar for his Gplinks Bot !!
'''

# Bitly Bot

import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyshorteners import Shortener
from config import *
from sample_config import Config

BITLY_KEY = "96bbcd78781ecd9018670be6c876452af049084a"
API_ID=10293305
API_HASH = "9b3bb6ac48fbbc1195e4657fe30858e9"
BOT_TOKEN = "5519560955:AAHkEKKpNMIoptfSbk9vV5q-Wh5XTOmg8n4"
USERS = ("1802569102 1016768333").split(" ")


SHORTLINKBOT = Client('ShortlinkBot',
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             workers=50,
             sleep_threshold=10)
             
             

@SHORTLINKBOT.on_message(filters.command(['start','help']) & filters.user(Config.USERS))
async def start(_, update):
    markup = InlineKeyboardMarkup([[InlineKeyboardButton("Made By", url=f"https://t.me/{OWNER}")]])
    await update.reply(
        f"**Hi {update.chat.first_name}!**\n"
        "I Am A Bitly Short Link Generator For Few Users",
        reply_markup=markup,
        quote=True)

@SHORTLINKBOT.on_message(filters.regex(r'https?://[^\s]+')) & filters.user(Config.USERS)
async def link_handler(_, update):
    link = update.matches[0].group(0)
    shortened_url, Err = get_shortlink(link)
    if shortened_url is None:
        message = f"Something Went Wrong \n{Err}"
        await update.reply(message, quote=True)
        return
    message = f"**Here Is Your ShortLink :** {shortened_url}"
    markup = InlineKeyboardMarkup([[InlineKeyboardButton("Link", url=shortened_url)]])
    # i don't think this bot with get sending message error so no need of exceptions
    await update.reply_text(text=message, reply_markup=markup, quote=True)
      
def get_shortlink(url):
    shortened_url = None
    Err = None
    try:
       if BITLY_KEY:
           ''' Bittly Shorten'''
           s = Shortener(api_key=BITLY_KEY)
           shortened_url = s.bitly.short(url)
       else:
           ''' Da.gd : I prefer this '''
           s = Shortener()
           shortened_url = s.dagd.short(url)
    except Exception as error:
        Err = f"#ERROR: {error}"
        log.info(Err)
    return shortened_url,Err
        
        
if __name__ == "__main__" :
    log.info(">>Bot-Started<<")
    SHORTLINKBOT.run()
