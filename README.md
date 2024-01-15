# Adlinkfly Telegram Bot

### A Simple to Use Python based Telegram Bot Script designed to work with Adlinlfly PHP Link Shortener Website using the Adlinkfly Developer API!<br></br>
[![status](https://img.shields.io/badge/status-active-brightgreen.svg?style=flat)](https://github.com/techishfellow/adlinkfly-telegram-bot)
[![release verion](https://img.shields.io/badge/release-v2.1.0-yellow.svg?style=flat)](https://github.com/techishfellow/adlinkfly-telegram-bot/releases/)
[![python version](https://img.shields.io/badge/python-v3.11.x-blue.svg?style=flat)](https://www.python.org/downloads/)
<br></br>

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/techishfellow/adlinkfly-telegram-bot.git)

**⚡ Requirements:**

1. Python Packages:
   * [pyTelegramBotAPI](https://pypi.org/project/pyTelegramBotAPI/)
   * [telebot](https://pypi.org/project/telebot/)
   * [requests](https://pypi.org/project/requests/)
   * [regex](https://pypi.org/project/regex/)
   * [Flask](https://pypi.org/project/Flask/)
   * [threaded](https://pypi.org/project/threaded/)
   * [gunicorn](https://pypi.org/project/gunicorn/)
   * [python-dotenv](https://pypi.org/project/python-dotenv/)
2. Must have a Adlinkfly Link Shortener Website hosted on the web with a valid domain name
3. Your Adlinkfly website has a valid SSL Certificate installed (Accessable via HTTPS protocol!)
4. Must have configured a suitable runtime envioronment to run python scripts!
(Recommended: Render, Koyeb, Replit -OR- Any Python Compatible Web Server)

**🏷️ Features:**
* Easy to Integrate and Customiseable (All-in-One Config File!)
* Auto URL Detection and Shortening (No extra commands needed! Just send the link to shorten...It's too easy..!!)
* Auto userinput Link Validation with Error Messages.
* Available Telegram Commands:
  * **/start** - Shows a custom welcome message when user starts the first conversation with the bot
  * **/help** - Shows a custom help and support message when the /help command is given by the user
  * **/ads** - Shortens the link with Ads. Also creates a separate Short Link Page!
  (* By default the link shortening method is set to *Direct Shortening without any Ads and Short Link Page*, if the User wants to shorten the link with *Ads and Short Link Page* the /ads command is required everytime!)
* More features will be added soon! stay tuned...!!!

**🔽 Download and Demo:**
* **Demo:** See and interact with a live Adlinkfly Telegram Bot - (ProURL Infinity Bot) - [Chat with ProURL Infinity Bot](https://t.me/ProURL_bot)
* **Download:**
   * Download from the latest stable release:
      * For Replit Deployment:-  replit-adlinkfly-telegram-bot-vX.X.X.zip [Download Now](https://github.com/techishfellow/adlinkfly-telegram-bot/releases/)
      * For Normal Deployment:- adlinkfly-telegram-bot-vX.X.X.zip [Download Now](https://github.com/techishfellow/adlinkfly-telegram-bot/releases/)

**⚙️ Configurations:**

* **Replit Configuration Steps:**

   1. Download the latest stable replit-adlinkfly-telegram-bot release zip file
   2. Unzip the .zip archive using any archive manager software (Winrar, 7zip, ZArchiver etc.)
   3. No extra configuration needed.....just follow the Replit Installation Steps

* **Normal Configuration Steps:**
   
   1. Download the latest stable adlinkfly-telegram-bot release zip file
   2. Unzip the .zip archive using any archive manager software (Winrar, 7zip, ZArchiver etc.)
   3. Open the ' .env ' file with any text or code editor
   4. Replace the below field values with yours!
   * Important Fields:
      * DOMAIN_NAME = Write the Domain Name of your Adlinkfly Website (Write nacked domain name without: www,  http://,  https://) (eg: yourdomain.com)
      * API_TOKEN = Paste your Telegram Bot API Token Here.
      Don't know how to get one? read [Here](https://dash11.comm100.io/kb/100/f9627b0c-6ff8-45c5-bdf5-b627f234d9bf/a/c8c7d736-f458-42ff-a863-f41b24fa5d02/where-do-i-find-telegram-bot-token)
      * ADLINKFLY_TOKEN = Paste your Adlinkfly Developer API Token Here.
      Don't know how to get one? read [Here](https://docs.mightyscripts.com/adlinkfly/#api_tools)
   * Custom Messages:
      * START = Write the custom message you want to show to the user when they use the telegram command **' /start '**
      * HELP = Write the custom message you want to show to the user when they use the telegram command **' /help '**
      * Further customization of commands is possible by modifying the python source code....if you want you can try...!!!<br></br>


**✔️ Installation:**
 * We recommend you to use [Replit](https://replit.com) + [UptimeRobot](https://uptimerobot.com) to run your Adlinkfly Telegram Bot 24/7 for absolutely Free of Cost!

     * **Replit Installation Steps** :
        1. Required installation files  - 2 Files: 'main.py', 'webserver.py'. (Optional Packager files: 'poetry.lock' and 'pyproject.toml' will be created automatically by Replit)

        2. Visit Replit and create a New Public Project selecting the Python Runtime Environment

        3. Navigate to the left 'Files' Sidebar click on the 'three dots', choose 'Upload file' option and upload the downloaded 'main.py', 'webserver.py' files one by one

        4. Now navigate to the 'Tools' section and choose 'Secrets' then create these 5 SECRET_KEY named: DOMAIN_NAME, BOT_TOKEN, ADLINKFLY_TOKEN, START, HELP (Fill up your own values on the value field of the Secrets - Read the Normal Configaration Steps section point (iv) for more info)

        5. Then navigate to the 'Packages' section and make sure to install all the required python packages mentioned earlier at the top (Just search the packages and click install)

        6. Now at this point you are all set to start the bot. Just click on the green 'Run' button at the top (An 'Webview' page will be created automatically and it will display 'Adlinkfly Telegram Bot is Running')

        7. Now copy the 'Webview' URL and visit the UptimeRobot website. If you don't have an account just create one and set a HTTPS Monitor to the copied URL (It will ping the Raplit server every 5Min to keep your bot up and running for 24/7)

     * **Normal Installation Steps** :

        1. The main installation files are - 3
        Files: 'main.py', 'webserver.py' and '.env'

        2. Make sure to configure the '.env' file as shown earlier on the 'Normal Installation Configuration' section

        3. Upload the main 3 files to your server Root -OR- Project Root directory (Must remember the server URL)

        4. Make sure to install all the required python packages mentioned earlier at the top (Via your package manager - Recommend: pip)

        5. Now at this point you are all set to start the bot. If you are using (PythonAnywhare, Heroku etc.) then just 'Run' the script. If you are using your own web server then you don't need to do anything else

        6. If you are using (PythonAnywhare, Heroku -OR- Your Web Server have Hibernation) then head over to UptimeRobot website: Create your account and set a HTTPS Monitor to your Server URL
        (It will ping the Server every 5Min to keep your bot up and running for 24/7!)

***
**An Open Sourced Project** - Developed with &hearts; by **Subhamoy**
