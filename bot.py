#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os

import sys
import telepot
import time
from functools import reduce
from telepot.loop import MessageLoop

TOKEN = ""
FORM_CHAT = 0
TO_CHAT = 0

if os.path.isfile('config.json'):
    with open('config.json', 'r') as f:
        config = json.load(f)
        if config['token'] == "":
            sys.exit("No token defined. Define it in a file called config.json.")
        if config['from'] == 0:
            sys.exit("No from defined. Define it in a file called config.json.")
        if config['to'] == 0:
            sys.exit("No to defined. Define it in a file called config.json.")
        TOKEN = config['token']
        FORM_CHAT = config['from']
        TO_CHAT = config['to']
else:
    sys.exit("No config file found. Remember changing the name of config-sample.json to config.json")

def log(msg, reason):
    f = open('logs.log', 'a')
    f.write(f"{reason}:\r\n{msg}\r\n")


def contains_link(msg):
    result = 'entities' in msg and reduce(
        lambda result, entity: result or (entity['type'] == 'url'), 
        msg['entities'], 
        False
    )
    if not result:
        log(msg, 'has no link')
    return result

def from_correct_chat(msg):
    result = msg['chat']['id'] == FORM_CHAT
    if not result:
        log(msg, 'came from wrong chat')
    return result

def is_editted(msg):
    result = 'edit_date' in msg
    if result:
        log(msg, 'has been edited')
    return result

def handle(msg):
    if from_correct_chat(msg) and not is_editted(msg) and contains_link(msg):
        print(f"trying to forward {msg['message_id']} from {msg['chat']['id']} to {TO_CHAT}")
        bot.forwardMessage(TO_CHAT, msg['chat']['id'], msg['message_id'])

bot = telepot.Bot(TOKEN)

MessageLoop(bot, handle).run_as_thread()
print('Listening...')
# Keep the program running.
while 1:
    time.sleep(10)
