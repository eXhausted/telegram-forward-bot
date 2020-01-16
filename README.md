# telegram-forward-bot
Simple Telegram Bot for forwarding messages with urls easily from one group to another in one-way.

Made with latest version of telepot at the time (12.0) and for Python 3.5.2. And shared with a MIT license.

## How to install

We will assume you and your friends have Telegram accounts and several telegram chats.

First, you need to create a Telegram bot. Talk with the [BotFather](https://t.me/botfather) and ask it for a bot (and its respective token)

Then, you need to rename the file config-sample.json to config.json. Add in `token` property your bot's token. Add in `from` property your source group id. Add in `to` property your desitanion group id.

The next part is to install in your server the requirements of the bot using `pip3 install -r requirements.txt`.

finally, configure the bot, adding it on all the groups you want to connect

## How to use

1. Add bot into two groups
2. Launch `bot.py`



