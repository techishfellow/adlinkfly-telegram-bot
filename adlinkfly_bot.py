from webserver import keep_alive
from dotenv import load_dotenv
from urllib.parse import quote
import json
import os
import re
import requests
import telebot
#this script is designed to work with a adlinkfly php link shortener website! for more info read the ' readme.md ' file...!!
#this script is developed by @neo_subhamoy
#website: https://neosubhamoy.com

load_dotenv()   #load environment variables from .env file

DOMAIN = os.environ.get('DOMAIN_NAME') or os.getenv('DOMAIN_NAME')
API_KEY = os.environ.get('BOT_TOKEN') or os.getenv('BOT_TOKEN')
ADLINKFLY_KEY = os.environ.get('ADLINKFLY_TOKEN') or os.getenv('ADLINKFLY_TOKEN')
START = os.environ.get('START') or os.getenv('START')
HELP = os.environ.get('HELP') or os.getenv('HELP')
START_MESSAGE = START.replace("\\n", "\n")
HELP_MESSAGE = HELP.replace("\\n", "\n")

bot = telebot.TeleBot(API_KEY)    #create bot instance

#function for No Ads shortening API call
def shorten_link(link):
  try:
    r = requests.get(f'https://{DOMAIN}/api?api={ADLINKFLY_KEY}&url={link}&type=0')

    if r.status_code == 200:
      response = json.loads(r.text)
      return response['shortenedUrl']
    else:
      print(f'Request failed with status code: {r.status_code}')
      print(f'Response content: {r.text}')
      return None

  except Exception as e:
    print(f'An error occurred: {str(e)}')
    return None

#function for With Ads shortening API call
def shorten_link_withads(link):
  try:
    r = requests.get(f'https://{DOMAIN}/api?api={ADLINKFLY_KEY}&url={link}')

    if r.status_code == 200:
      response = json.loads(r.text)
      return response['shortenedUrl']
    else:
      print(f'Request failed with status code: {r.status_code}')
      print(f'Response content: {r.text}')
      return None

  except Exception as e:
    print(f'An error occurred: {str(e)}')
    return None

#function to check if the (UserInput) Link is Valid
def is_valid_url(link):
  url_regex = re.compile(
    r'^(?:http|ftp)s?://'
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
    r'localhost|'
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
    r'(?::\d+)?'
    r'(?:/?|[/?]\S+)$',
    re.IGNORECASE)
  return url_regex.match(link)


@bot.message_handler(commands=['start'])
def start(message):
  bot.reply_to(
      message,
      START_MESSAGE,
      parse_mode='Markdown',
      disable_web_page_preview=True)
  bot.send_message(
      message.chat.id,
      "Yay! I\'m too exited to see you..!!\nJust send me a link to see the magic..."
  )


@bot.message_handler(commands=['help'])
def help(message):
  bot.reply_to(
      message,
      HELP_MESSAGE
  )


@bot.message_handler(commands=['ads'])
def handle_nometa_command(message):
  bot.send_message(
      chat_id=message.chat.id,
      text="Please send the link to shorten without URL metadata!")
  bot.register_next_step_handler(message, handle_link)


def handle_link(message):
  if is_valid_url(message.text):
    bot.send_message(message.chat.id, "Shortening! Please wait...")
    link = quote(message.text)    #urlencode the link
    shortened_link = shorten_link_withads(link)    #shorten the link (With Ads)
    if shortened_link:
      bot.reply_to(message,
                   "Link Metadata Removed!\n" + shortened_link,
                   parse_mode='Markdown',
                   disable_web_page_preview=True)
    else:
      bot.reply_to(message, 'Failed to shorten the link! Please try again...')
  else:
    bot.send_message(
        message.chat.id,
        "Invalid URL!\nPlease reuse the command /nometa to try again with a valid link..."
    )


@bot.message_handler(content_types=['text'])
def handle_text(message):
  if is_valid_url(message.text):
    bot.send_message(message.chat.id, "Shortening! Please wait...")
    link = quote(message.text)    #urlencode the link
    shortened_link = shorten_link(link)    #shorten the link (No Ads)
    if shortened_link:
      bot.reply_to(message,
                   shortened_link,
                   parse_mode='Markdown',
                   disable_web_page_preview=True)
    else:
      bot.reply_to(message, 'Failed to shorten the link! Please try again...')
  else:
    bot.send_message(message.chat.id,
                     "Invalid URL!\nPlease send a valid link...!")


keep_alive()
bot.polling()
