# Adlinkfly Telegram Bot

### A Simple to Use Python based Telegram Bot Script designed to work with Adlinlfly PHP Link Shortener Website using the Adlinkfly Developer API!<br></br>
[![status](https://img.shields.io/badge/status-active-brightgreen?style=flat)](https://github.com/techishfellow/adlinkfly-telegram-bot)
[![github tag](https://img.shields.io/github/v/tag/techishfellow/adlinkfly-telegram-bot?color=yellow)](https://github.com/techishfellow/adlinkfly-telegram-bot/releases/)
[![python version](https://img.shields.io/badge/python-v3.13-blue?logo=python&style=flat)](https://www.python.org/downloads/)
<br></br>

### **⚡ 1-Click Deployment:**

[![Deploy to Koyeb](https://img.shields.io/badge/deploy%20to%20koyeb-2c7653?style=for-the-badge&logo=koyeb)](https://app.koyeb.com/deploy?type=git&repository=github.com/techishfellow/adlinkfly-telegram-bot&branch=main&name=adlinkfly-telegram-bot&service_type=web&instance_type=free&ports=8080;http;/&env[DOMAIN_NAME]=yourDomainName&env[BOT_TOKEN]=yourTelegramBotApiToken&env[ADLINKFLY_TOKEN]=yourAdlinkflyApiToken&env[START]=yourStartMessage&env[HELP]=yourHelpMessage&run_command=python3%20adlinkfly_bot.py)
[![Deploy to Render](https://img.shields.io/badge/deploy%20to%20render-8a05ff?style=for-the-badge&logo=render&logoColor=ffffff)](https://render.com/deploy?repo=https://github.com/techishfellow/adlinkfly-telegram-bot.git)

* 1-click deployment is the easiest way to deploy this bot! Click on these buttons to deploy the bot in corresponding platform. Just make sure to fill-up/replace proper environmental variable values when asked. Parameters are explained below in details (in Configuration / Environment Vriables section).

### **📌 Requirements:**

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
4. Must have configured a suitable runtime envioronment (WSGI Compatible) to run python scripts!
(Recommended: Render, Koyeb, Replit -OR- A Docker Container in your Custom Server)

### **🏷️ Features:**

* Easy to Integrate and Customiseable (All-in-One Config File!)
* Auto URL Detection and Shortening (No extra commands needed! Just send the link to shorten...It's too easy..!!)
* Supports Link Shortening with Custom Alias
* Auto userinput Link Validation with Error Messages.
* Available Telegram Commands:
  * **/start** - Shows a custom welcome message when user starts the first conversation with the bot
  * **/help** - Shows a custom help and support message when the /help command is given by the user
  * **/ads** - Shortens the link with Ads. Also creates a separate Short Link Page!
  (* By default the link shortening method is set to *Direct Shortening without any Ads and Short Link Page*, if the User wants to shorten the link with *Ads and Short Link Page* the /ads command is required everytime!)
  * **/alias** - Shortens the link with a custom alias of your choice (eg: yourdomain.com/cool-alias)
  * **/alias-ads** - Shortens the link with a custom alias of your choice and also creates a separate Short Link Page which *includes Ads*

### **🔽 Download:**

   * You don't need to download anything for most cases (except: you are deploying this in your own custom server directly)
   * For Custom Server deployment (direct) Download the Latest ZIP from Releases Section: adlinkfly-telegram-bot-vX.X.X.zip [Download Now](https://github.com/techishfellow/adlinkfly-telegram-bot/releases/)

### **⚙️ Configuration / Environment Vriables:**
   
   * There is only one global configuration file ' .env ' also known as Environment Variables  which you need to configure for your bot! An example of available fields are shown in ' .env.example ' file and also described below (If you are using the 1-click deployment solutions you don't need to create any separate ' .env ' file. All the KEYs are predefined for you! You just need to input/replace their values when asked)
   
   ```code
   HOST_PORT = 8080   #Only for Docker Container Deployment - OPTIONAL - DEFAULT: 8080
   DOMAIN_NAME = yourdomain.com
   BOT_TOKEN = Paste Your Telegram Bot API Token
   ADLINKFLY_TOKEN = Paste Your Adlinkfly API Token

   START = Type the start message here you want to show the user \nNew Line Starts Here
   HELP = Type the help message here you want to show the user \nNew Line Starts Here

   #Don't use https:// on DOMAIN_NAME field just type the nacked domain name as shown!
   #To change the line (New Line) of START or HELP message use ' \n ' between the lines (Works as Enter Key of Keyboard! Python Syntax... :-)
   ```
   
   * Important Fields:
      * DOMAIN_NAME = Write the Domain Name of your Adlinkfly Website (Write nacked domain name without: www,  http://,  https://) (eg: yourdomain.com)
      * API_TOKEN = Paste your Telegram Bot API Token Here.
      Don't know how to get one? read [Here](https://dash11.comm100.io/kb/100/f9627b0c-6ff8-45c5-bdf5-b627f234d9bf/a/c8c7d736-f458-42ff-a863-f41b24fa5d02/where-do-i-find-telegram-bot-token)
      * ADLINKFLY_TOKEN = Paste your Adlinkfly Developer API Token Here.
      Don't know how to get one? read [Here](https://docs.mightyscripts.com/adlinkfly/#api_tools)
   * Optional Fields:
      * HOST_PORT = Maps the internal Docker Container Port (8080) to the specified port in your host machine. Useful when another process is running on the same port in your host machine for some reason, which may lead to malfunction. By default it uses the same port (8080) of your host machine which can be overwritten by this variable
   * Custom Messages:
      * START = Write the custom message you want to show to the user when they use the telegram command **' /start '**
      * HELP = Write the custom message you want to show to the user when they use the telegram command **' /help '**
      * Further customization of commands is possible by modifying the python source code....if you want you can try...!!!<br></br>


### **🚀 Installation / Deployment:**

  * **1-Click Deployment (Easiest):**
    1. Just click on any one of the button given at the top (in which platform you want to deploy) and follow the steps. NOTE: Make sure to Login the platform first before clicking on the button
    2. You will be asked to fill-up the Environment Variable values (check Configuration / Environment Vriables section for more info) Fill-up the values properly and proceed. That's it...!!
    * Your platform is not listed? -> I'm continuously trying to integrate more and more platforms. But, if it's still not listed You can try the custom deployment option or contact me for further info.
  * **Replit Deployment:**
    1. Use 'Import from GitHub' option to import this repo. Don't know how to do so? read [Here](https://docs.replit.com/hosting/deployments/deploying-a-github-repository)
    * Use this URL to Import:
    ```code
    https://github.com/techishfellow/adlinkfly-telegram-bot.git
    ```
    * Use this run command:
    ```code
    python3 adlinkfly_bot.py
    ```
    2. Open a 'Shell' window and run this command to install all dependencies:
    ```code
    pip install -r requirements.txt
    ```
    3. Open a 'Secrets' window and configure all secrets as explained earlier (in Configuration / Environment Vriables section). Replit Secrets works the same as Environment Variables. Don't know how to use Replit Secrets? read [Here](https://docs.replit.com/programming-ide/workspace-features/secrets)

    4. Now just click on the green 'Run' button at the top to start the bot. That's it...!!
  * **Custom Server Deployment (With Docker) (Recommended):**
    1. Install Docker and Docker Compose Plugin (on Ubuntu / Debian):
    ```code
    curl -sSL https://get.docker.com/ | CHANNEL=stable sh && apt install docker-compose-plugin
    ```
    2. Clone the Adlinkfly Telegram Bot Git Repository to /opt/adlinkfly-telegram-bot:
    ```code
    git clone https://github.com/techishfellow/adlinkfly-telegram-bot.git /opt/adlinkfly-telegram-bot
    ```
    3. Navigate to /opt/adlinkfly-telegram-bot then create a blank .env file and modify it (as explained earlier, in Configuration / Environment Vriables section) using command line text editor nano:
    ```code
    cd /opt/adlinkfly-telegram-bot && touch /opt/adlinkfly-telegram-bot/.env && nano /opt/adlinkfly-telegram-bot/.env
    ```
    Save it with `CTRL` + `O` and then pressing `Enter`, Exit nano `CTRL` + `X`
    
    4. Not to build and start Adlinkfly Telegram Bot, go to /opt/adlinkfly-telegram-bot then build and launch the docker containers:
    ```code
    cd /opt/adlinkfly-telegram-bot && docker compose build && docker compose up -d
    ```
    5. To STOP the bot you can use this command anytime:
    ```code
    cd /opt/adlinkfly-telegram-bot && docker compose down
    ```
  * **Custom Server Deployment (Directly) (Not Recommended):**
    * IMPORTANT: This script only works in WSGI Compitable Servers (Most Linux Distros will work fine...!! Windows is not supported...!!)
    1. Unzip the downloaded release ZIP file (using any zip extractor software. eg: WinRAR, 7zip etc.)
    2. Open the extracted folder and Create a new ' .env ' file on that location and configure it as explained earlier (in Configuration / Environment Vriables section) (Use any text editor software or terminal text editors. eg: notepad, vim, nano)
    3. Upload all the extracted files along with the .env file in your server root
    4. Make sure you have already installed **python3** and **pip** in your server (Most linux distros comes with python3 pre-installed. You just need to install pip) To install pip with apt package manager in Ubuntu run this below command in your server terminal:
    ```code
    sudo apt install python3-pip
    ```
    5. Now, to install all the dependencies run this command:
    ```code
    pip install -r requirements.txt
    ```
    6. Now, to start the bot run this command:
    ```code
    python3 adlinkfly_bot.py
    ```
    7. **To, STOP the bot you can use CTRL + C or this command:**
    ```code
    pkill -SIGINT -f 'gunicorn -b 0.0.0.0:8080 -w 4 webserver:adlinkflytgbot'
    ```

### **🛠️ Contributing / Building from Source:**
  * Want to be the part of this project? Feel free to contribute..!! Pull Requests are always welcome....!! Follow this simple steps to start building . . .
  * Using Linux Development Environment is Required | for Windows use WSL or just spin up a Docker Container
  1. Fork this repo in your github account
  2. Git clone the forked repo in your local machine
  3. Create your .env file as explained earlier
  4. Install all dependencies:
  ```code
  pip install -r requirements.txt
  ```
  5. Run the bot:
  ```code
  python3 adlinkfly_bot.py
  ```
  6. Do the changes, Send a Pull Request with proper Description (NOTE: Pull Requests Without Proper Description will be Rejected)

### **📝 License & Usage**

Adlinkfly Telegram Bot is an Open Sourced Project Licensed under GPL-3.0 Anyone can View, Modify or Use (Personal and Commercial) it's Sources without any extra permissions. If you want to Distribute it's Sources then please consider giving it an attribution of this repo.
NOTE: This Script is Not Officially developed, supported or affiliated by MightyScripts. This is just a hobby project of mine!

***

**An Open Sourced Project** - Developed with &hearts; by **Subhamoy**
