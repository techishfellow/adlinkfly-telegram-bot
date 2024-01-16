from flask import Flask
from threading import Thread
import subprocess
#this file is used to host and run your telegram bot 24/7 on a webserver.
#this script is developed by @neo_subhamoy
#website: https://neosubhamoy.com

adlinkflytgbot = Flask('Adlinkfly Telegram Bot')

@adlinkflytgbot.route('/')
def home():
  return "Adlinkfly Telegram Bot is Running!"

def run_gunicorn():
    gunicorn_command = [
        'gunicorn',
        '-b', '0.0.0.0:8080',
        '-w', '4',
        'webserver:adlinkflytgbot',
    ]
    subprocess.Popen(gunicorn_command)

def keep_alive():
    t = Thread(target=run_gunicorn)
    t.start()