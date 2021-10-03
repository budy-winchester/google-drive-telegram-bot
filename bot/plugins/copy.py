from pyrogram import Client, filters
from bot.config import BotCommands, Messages
from bot.helpers.utils import CustomFilters
from bot.helpers.gdrive_utils import GoogleDrive
from bot import LOGGER
import requests

@Client.on_message(filters.private & filters.incoming & filters.command(BotCommands.Clone) & CustomFilters.auth_users)
def shorten_url(url):
	base_url = "http://ouo.io/api/ARlk1o6H?s="
	url = base_url + url
	print('Original URL', url)
	r = requests.get(url).text

def _clone(client, message):
  user_id = message.from_user.id
  if len(message.command) > 1:
    url = message.command[1]
    LOGGER.info(f'Copy:{user_id}: {url}')
    sent_message = message.reply_text(Messages.CLONING.format(url), quote=True)
    link2 = shorten_url(url)
    msg = GoogleDrive(user_id).clone(link2)
    sent_message.edit(msg)
  else:
    message.reply_text(Messages.PROVIDE_GDRIVE_URL.format(BotCommands.Clone[0]))
