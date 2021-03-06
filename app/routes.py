from flask import request
import telebot

from app import bot, app


@app.route('/', methods=['POST'])
def index():
    if request.method == 'POST':
        update = telebot.types.Update.de_json(request.stream.read().decode("utf-8"))
        bot.bot.process_new_updates([update])
        return ""
