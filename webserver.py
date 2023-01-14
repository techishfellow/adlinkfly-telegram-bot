from flask import Flask
from threading import Thread
#this file is used to host and run your telegram bot 24/7 on a server with a weburl.
#this script is developed by @neo_subhamoy
#website: https://neosubhamoy.xyz

app = Flask('')

@app.route('/')
def home():
  return "Adlinkfly Telegram Bot is Running!"
def run():
  app.run(host='0.0.0.0', port=8080)
def keep_alive():
  t = Thread(target=run)
  t.start()