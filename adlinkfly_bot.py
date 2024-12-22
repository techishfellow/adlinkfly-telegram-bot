from webserver import keep_alive
from dotenv import load_dotenv
from urllib.parse import quote
import json
import os
import re
import requests
import telebot
#this script is designed to work with a adlinkfly php link shortener website! for more info read the ' README.md ' file...!!
#this script is developed by @neo_subhamoy
#website: https://neosubhamoy.com

load_dotenv()

DOMAIN = os.environ.get('DOMAIN_NAME') or os.getenv('DOMAIN_NAME')
API_KEY = os.environ.get('BOT_TOKEN') or os.getenv('BOT_TOKEN')
ADLINKFLY_KEY = os.environ.get('ADLINKFLY_TOKEN') or os.getenv('ADLINKFLY_TOKEN')
START = os.environ.get('START') or os.getenv('START')
HELP = os.environ.get('HELP') or os.getenv('HELP')
START_MESSAGE = START.replace("\\n", "\n")
HELP_MESSAGE = HELP.replace("\\n", "\n")

bot = telebot.TeleBot(API_KEY)
user_data = {}

#function for No Ads shortening API call with alias
def shorten_link_with_alias(link, alias):
    try:
        r = requests.get(f'https://{DOMAIN}/api?api={ADLINKFLY_KEY}&url={link}&alias={alias}&type=0')

        if r.status_code == 200:
            response = json.loads(r.text)
            if response['status'] != 'success':
                return None
            return response['shortenedUrl']
        else:
            print(f'Request failed with status code: {r.status_code}')
            print(f'Response content: {r.text}')
            return None

    except Exception as e:
        print(f'An error occurred: {str(e)}')
        return None

#function for With Ads shortening API call with alias
def shorten_link_withads_alias(link, alias):
    try:
        r = requests.get(f'https://{DOMAIN}/api?api={ADLINKFLY_KEY}&url={link}&alias={alias}')

        if r.status_code == 200:
            response = json.loads(r.text)
            if response['status'] != 'success':
                return None
            return response['shortenedUrl']
        else:
            print(f'Request failed with status code: {r.status_code}')
            print(f'Response content: {r.text}')
            return None

    except Exception as e:
        print(f'An error occurred: {str(e)}')
        return None

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

#function to check if alias is valid
def is_valid_alias(alias):
    alias_regex = re.compile(r'^[a-zA-Z0-9-]+$')
    return alias_regex.match(alias)

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
        HELP_MESSAGE,
        parse_mode='Markdown',
        disable_web_page_preview=True
    )

@bot.message_handler(commands=['ads'])
def handle_nometa_command(message):
    bot.send_message(
        chat_id=message.chat.id,
        text="Please send the link to shorten (with ads):")
    bot.register_next_step_handler(message, handle_link)

@bot.message_handler(commands=['alias'])
def handle_alias_command(message):
    bot.send_message(
        chat_id=message.chat.id,
        text="Please send the link to shorten with custom alias:")
    bot.register_next_step_handler(message, handle_alias_url)

def handle_alias_url(message):
    if is_valid_url(message.text):
        user_data[message.chat.id] = {'url': message.text}
        bot.send_message(
            message.chat.id,
            "Now, please send your desired alias (only letters, numbers, and hyphens allowed):")
        bot.register_next_step_handler(message, handle_alias_creation)
    else:
        bot.send_message(
            message.chat.id,
            "Invalid URL!\nPlease use /alias command again with a valid link..."
        )

def handle_alias_creation(message):
    if not is_valid_alias(message.text):
        bot.send_message(
            message.chat.id,
            "Invalid alias! Only letters, numbers, and hyphens are allowed.\nPlease use /alias command again..."
        )
        return

    chat_id = message.chat.id
    if chat_id not in user_data:
        bot.send_message(
            chat_id,
            "Something went wrong. Please start over with /alias command."
        )
        return

    long_url = user_data[chat_id]['url']
    alias = message.text
    
    bot.send_message(message.chat.id, "Shortening! Please wait...")
    shortened_link = shorten_link_with_alias(quote(long_url), alias)
    
    if shortened_link:
        bot.reply_to(
            message,
            f"Link Shortened With Custom Alias!\n{shortened_link}",
            parse_mode='Markdown',
            disable_web_page_preview=True
        )
    else:
        bot.reply_to(
            message,
            'Failed to create custom short link! The alias might be taken or there was an error. Please try again with a different alias.'
        )
    
    # Clean up user data
    del user_data[chat_id]

@bot.message_handler(commands=['alias_ads'])
def handle_alias_ads_command(message):
    bot.send_message(
        chat_id=message.chat.id,
        text="Please send the link to shorten with custom alias (with ads):")
    bot.register_next_step_handler(message, handle_alias_ads_url)

def handle_alias_ads_url(message):
    if is_valid_url(message.text):
        user_data[message.chat.id] = {'url': message.text}
        bot.send_message(
            message.chat.id,
            "Now, please send your desired alias (only letters, numbers, and hyphens allowed):")
        bot.register_next_step_handler(message, handle_alias_ads_creation)
    else:
        bot.send_message(
            message.chat.id,
            "Invalid URL!\nPlease use /alias_ads command again with a valid link..."
        )

def handle_alias_ads_creation(message):
    if not is_valid_alias(message.text):
        bot.send_message(
            message.chat.id,
            "Invalid alias! Only letters, numbers, and hyphens are allowed.\nPlease use /alias_ads command again..."
        )
        return

    chat_id = message.chat.id
    if chat_id not in user_data:
        bot.send_message(
            chat_id,
            "Something went wrong. Please start over with /alias_ads command."
        )
        return

    long_url = user_data[chat_id]['url']
    alias = message.text
    
    bot.send_message(message.chat.id, "Shortening! Please wait...")
    shortened_link = shorten_link_withads_alias(quote(long_url), alias)
    
    if shortened_link:
        bot.reply_to(
            message,
            f"Link Shortened With Custom Alias (with ads)!\n{shortened_link}",
            parse_mode='Markdown',
            disable_web_page_preview=True
        )
    else:
        bot.reply_to(
            message,
            'Failed to create custom short link! The alias might be taken or there was an error. Please try again with a different alias.'
        )
    
    # Clean up user data
    del user_data[chat_id]

def handle_link(message):
    if is_valid_url(message.text):
        bot.send_message(message.chat.id, "Shortening! Please wait...")
        link = quote(message.text)
        shortened_link = shorten_link_withads(link)
        if shortened_link:
            bot.reply_to(message,
                        "Link Shortened (with ads)!\n" + shortened_link,
                        parse_mode='Markdown',
                        disable_web_page_preview=True)
        else:
            bot.reply_to(message, 'Failed to shorten the link! Please try again...')
    else:
        bot.send_message(
            message.chat.id,
            "Invalid URL!\nPlease reuse the command /ads to try again with a valid link..."
        )

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if is_valid_url(message.text):
        bot.send_message(message.chat.id, "Shortening! Please wait...")
        link = quote(message.text)
        shortened_link = shorten_link(link)
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