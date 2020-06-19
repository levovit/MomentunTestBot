from time import sleep

import telebot
from telebot import types
from telebot.types import Message

from app import db, app
from app.keyboards import get_setting_keyboard, get_menu_keyboard, get_gender_keyboard
from app.models import User


bot = telebot.TeleBot(app.config["TOKEN"], threaded=False)
bot.remove_webhook()
sleep(1)
bot.set_webhook(url=app.config["HOST_URL"])


@bot.message_handler(commands=['start'])
def handle_start(message: Message):
    print(type(message))
    print(message.chat.id)
    user = User.query.filter_by(telegram_id=message.chat.id).first()
    print(user)
    if not user:
        print("not user")
        user = User(telegram_id=message.chat.id)
        db.session.add(user)
        db.session.commit()
        state = "name"
    else:
        print("user")
        state = user.state

    if state == "name" or state == "change name":
        text_message = "Enter your name"
    elif state == "age" or state == "change age":
        text_message = "Enter your age"
    elif state == "gender" or state == "change gender":
        text_message = "Enter your gender"
    else:
        text_message = "You are already registered"

    bot.send_message(message.chat.id, text_message)
    print(message.text, message.chat.username)


@bot.message_handler(commands=['reset'])
def handle_help(message: Message):
    user = User.query.filter_by(telegram_id=message.chat.id).first()
    if user:
        user.state = "name"
        db.session.commit()

    remove_keyboard = types.ReplyKeyboardRemove()

    bot.send_message(message.chat.id, "State annulled", reply_markup=remove_keyboard)
    print(message.text, message.chat.username)


@bot.message_handler(regexp="Back")
def back_to_menu(message: Message):
    text_message = "Back to Menu"
    menu_keyboard = get_menu_keyboard()

    bot.send_message(message.chat.id, text_message, reply_markup=menu_keyboard)


@bot.message_handler(regexp="📖️ My information")
def show_user_info(message: Message):
    user = User.query.filter_by(telegram_id=message.chat.id).first()
    if user:
        text_message = f"📖️ Your information\n\n" \
                       f"*name* - {user.name}\n" \
                       f"*age* - {user.age}\n" \
                       f"*gender* - {user.gender}\n"
    else:
        text_message = "sorry, you are not in DataBase"
    bot.send_message(message.chat.id, text_message, parse_mode="Markdown")
    print(message.text, message.chat.username)


@bot.message_handler(regexp="⚙️ settings")
def show_settings(message: Message):
    text_message = "⚙️ settings"
    settings_keyboard = get_setting_keyboard()
    bot.send_message(message.chat.id, text_message, reply_markup=settings_keyboard)
    print(message.text, message.chat.username)


@bot.message_handler(regexp="Change age")
def change_age(message: Message):
    text_message = "Enter your new age"
    remove_keyboard = types.ReplyKeyboardRemove()

    user = User.query.filter_by(telegram_id=message.chat.id).first()
    user.state = "change age"
    db.session.commit()

    bot.send_message(message.chat.id, text_message, reply_markup=remove_keyboard)


@bot.message_handler(func=lambda message: User.get_state_by_id(message.chat.id) == "change age")
def new_age(message: Message):
    text = message.text
    if not text.isdigit():
        bot.send_message(message.chat.id, "Must be integer")
        return
    else:
        age = int(text)
        user = User.query.filter_by(telegram_id=message.chat.id).first()
        user.age = age
        user.state = "done"
        db.session.commit()
        text_message = "Congratulations, you change age"
        settings_keyboard = get_setting_keyboard()
        bot.send_message(message.chat.id, text_message, reply_markup=settings_keyboard)


@bot.message_handler(regexp="Change name")
def change_name(message: Message):
    text_message = "Enter your new name"
    remove_keyboard = types.ReplyKeyboardRemove()

    user = User.query.filter_by(telegram_id=message.chat.id).first()
    user.state = "change name"
    db.session.commit()

    bot.send_message(message.chat.id, text_message, reply_markup=remove_keyboard)


@bot.message_handler(func=lambda message: User.get_state_by_id(message.chat.id) == "change name")
def new_age(message: Message):
    name = message.text

    len_text = len(name)
    if len_text < 2 or len_text > 20:
        text_message = "name must be between 2 and 20 characters"
        bot.send_message(message.chat.id, text_message)
        return
    else:
        user = User.query.filter_by(telegram_id=message.chat.id).first()
        user.name = name
        user.state = "done"
        db.session.commit()
        text_message = "Name changed successfully"
        settings_keyboard = get_setting_keyboard()
        bot.send_message(message.chat.id, text_message, reply_markup=settings_keyboard)


@bot.message_handler(regexp="Change gender")
def change_gender(message: Message):
    text_message = "Enter your new gender"

    user = User.query.filter_by(telegram_id=message.chat.id).first()
    user.state = "change gender"
    db.session.commit()

    gender_keyboard = get_gender_keyboard()

    bot.send_message(message.chat.id, text_message, reply_markup=gender_keyboard)


@bot.message_handler(func=lambda message: User.get_state_by_id(message.chat.id) == "change gender")
def new_gender(message: Message):
    gender = message.text
    if gender not in ("Male", "Female"):
        bot.send_message(message.chat.id, "Gender must be Male or Female")
        return
    else:
        user = User.query.filter_by(telegram_id=message.chat.id).first()
        user.gender = gender
        user.state = "done"
        db.session.commit()
        text_message = "Gender changed"
        settings_keyboard = get_setting_keyboard()
        bot.send_message(message.chat.id, text_message, reply_markup=settings_keyboard)


@bot.message_handler(func=lambda message: User.get_state_by_id(message.chat.id) == "name")
def user_entering_name(message: Message):
    text = message.text

    len_text = len(text)
    if len_text < 2 or len_text > 20:
        text_message = "name must be between 2 and 20 characters"
    else:
        bot.send_message(message.chat.id, "Great name")
        user = User.query.filter_by(telegram_id=message.chat.id).first()
        user.name = text
        user.state = "age"
        db.session.commit()
        text_message = "Now, enter your age"

    bot.send_message(message.chat.id, text_message)
    print(message.text, message.chat.username)


@bot.message_handler(func=lambda message: User.get_state_by_id(message.chat.id) == "age")
def user_entering_age(message: Message):
    text = message.text
    if not text.isdigit():
        bot.send_message(message.chat.id, "Must be integer")
        return
    else:
        age = int(text)
        user = User.query.filter_by(telegram_id=message.chat.id).first()
        user.age = age
        user.state = "gender"
        db.session.commit()
        text_message = "And, enter your gender"
        gender_keyboard = get_gender_keyboard()

    bot.send_message(message.chat.id, text_message, reply_markup=gender_keyboard)
    print(message.text, message.chat.username)


@bot.message_handler(func=lambda message: User.get_state_by_id(message.chat.id) == "gender")
def user_entering_gender(message: Message):
    gender = message.text
    if gender not in ("Male", "Female"):
        bot.send_message(message.chat.id, "Gender must be Male or Female")
        return
    else:
        user = User.query.filter_by(telegram_id=message.chat.id).first()
        user.gender = gender
        user.state = "done"
        db.session.commit()
        text_message = "Thank you for registering!"

    menu_keyboard = get_menu_keyboard()

    bot.send_message(message.chat.id, text_message, reply_markup=menu_keyboard)
    print(message.text, message.chat.username)
