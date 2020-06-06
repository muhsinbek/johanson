# GLOBALS.py - no joke, it is just a bunch of global variables

import telebot
dev = 605321747  # replace this with your ID, it is my ID (@FutureDreams)
bot_id = 1177850370  # replace this with your bot's ID, this is actually @Hopsrobot's ID
python_uz = -1333450079  # this is the ID of our Python UZBEKISTAN group: @python_uz
test_group = -1250531807  # this is the ID of private tet group, change it to yours
allowed_groups = [python_uz, test_group, -1333450079, -1250531807]  # modify this to allow groups
verified = [dev]  # modify this to add verified accounts, verified accounts won't get banned or restricted
should_log = True  # set it to False, and log function doesn't work
botlink = 'kiufrobot'  # if your bot is @wonerbot, just write 'wonderbot'
token = "1177850370:AAGrWQRycnq_769EXnRUhNJNNyRdGxnNvvU"  # this is your bot's token which you can get from @Botfather
telegraph_token = '59cba89442c4eb201c7c71fff9379931121c18153777d7125f1c7526de9e'  # your Telegraph accounts' token, Google it to get more info
bot = telebot.TeleBot(token)  # single instance of bot
