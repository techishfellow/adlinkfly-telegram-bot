FROM ubuntu

RUN apt update && apt install -y python3 python3-pip
WORKDIR /opt/adlinkfly-telegram-bot

COPY requirements.txt .

RUN pip3 install -r requirements.txt --no-cache-dir --break-system-packages

COPY . .

ENTRYPOINT ["python3", "adlinkfly_bot.py"]