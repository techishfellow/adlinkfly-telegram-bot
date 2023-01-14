# Adlinkfly Python Telegram Bot

### A Simple to Use Python based Telegram Bot Script designed to work with Adlinlfly PHP Link Shortener Website using the Adlinkfly Developer API!<br></br>
**✨ Relese Version:** 1.0.7<br></br>
**⚡ Requirements:**

1. Python Packages:
   * [pyTelegramBotAPI](https://pypi.org/project/pyTelegramBotAPI/)
   * [telebot](https://pypi.org/project/telebot/)
   * [requests](https://pypi.org/project/requests/)
   * [regex](https://pypi.org/project/regex/)
   * [Flask](https://pypi.org/project/Flask/)
   * [threaded](https://pypi.org/project/threaded/)
2. Must have a Adlinkfly Link Shortener Website hosted on the web with a valid domain name
3. Your Adlinkfly website has a valid SSL Certificate installed (Accessable via HTTPS protocol!)
4. Must have configured a suitable runtime envioronment to run python scripts!
(Recommended: Replit, PythonAnywhare, Heroku)

**🏷️ Features:**
* Easy to Integrate and Customiseable (Aii-in-One Config File!)
* Auto URL Detection and Shortening (No extra commands needed! Just send the link to shorten...Too easy right..?)
* Auto userinput Link Validation with Error Messages.
* Available Telegram Commands:
  * **/start** - Shows a custom welcome message when user starts the first conversation with the bot
  * **/help** - Shows a custom help and support message when the /help command is given by the user
  * **/ads** - Shortens the link with Ads. Also creates a separate Short Link Page!
  (* By default the link shortening method is set to *Direct Shortening without any Ads and Short Link Page*, if the User wants to shorten the link with *Ads and Short Link Page* the /ads command is required everytime!)
* More features will be added soon! stay tuned...!!!

**⚙️ Configurations:**
1. Open the ' .env ' file with any text or code editor
2. Replace the below field values with your informations!
 * Important Fields:
   * DOMAIN_NAME = Write the Domain Name of your Adlinkfly Website
   * API_TOKEN = Paste your Telegram Bot API Token Here.
   Don't know how to get one? read [Here](https://dash11.comm100.io/kb/100/f9627b0c-6ff8-45c5-bdf5-b627f234d9bf/a/c8c7d736-f458-42ff-a863-f41b24fa5d02/where-do-i-find-telegram-bot-token)
   * ADLINKFLY_TOKEN = Paste your Adlinkfly Developer API Token Here.
   Don't know how to get one? read [Here](https://docs.mightyscripts.com/adlinkfly/#api_tools)
 * Custom Messages:
   * START = Write the custom message you want to show to the user when they use the telegram command **' /start '**
   * HELP = Write the custom message you want to show to the user when they use the telegram command **' /help '**<br></br>

* **IMPORTANT:** If you are using *Replit* to run this script! Unfortunately creation of ' .env ' file is now prohibited. First you need to store the Key and the Values separately using the *' Secrets '* option provided by Replit. Then import the secrets to the 'main.py' file to use them. for more info read [Here](https://docs.replit.com/programming-ide/storing-sensitive-information-environment-variables)

**✔️ Installation:**
1. We recommend you to use [Raplit](https://replit.com) + [UptimeRobot](https://uptimerobot.com) to run your Adlinkfly Telegram Bot 24/7 for absolutely Free of Cost!

2. The main installation files are - 3
Files: 'main.py', 'webserver.py' and '.env'
Optional Files:  'poetry.lock' and 'pyproject.toml'
(Optional files are created automatically by Replit)

3. Visit Replit and create a New Project selecting the Python Runtime Environment

4. Upload or Copy-Paste the previously configured main files and hit the Run Button
(Dont forget to replase the .env File with Replit Secrets!) Congratulations your bot is now running successfully...!

5. Now visit UptimeRobot website and set a HTTPS Monitor for your Flask Replit Server URL!
(It will ping every 5 min to the server to avoid Replit the server hybernation!)

***
🔗 **An Open Sourced Project** - Developed with &hearts; by **Subhamoy**
