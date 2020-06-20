from telebot import types

from app import commands_const as cc


def get_setting_keyboard():
    settings_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    settings_keyboard.row(*[types.KeyboardButton(text=i) for i in (cc.CHANGE_NAME, cc.CHANGE_AGE, cc.CHANGE_GENDER)])
    settings_keyboard.add(types.KeyboardButton(text=cc.BACK))
    return settings_keyboard


def get_menu_keyboard():
    menu_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    menu_keyboard.row(types.KeyboardButton(text=cc.MY_INFORMATION), types.KeyboardButton(text=cc.SETTINGS))
    return menu_keyboard


def get_gender_keyboard():
    gender_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    gender_keyboard.add(*[types.KeyboardButton(text=i) for i in cc.GENDER_LIST])
    return gender_keyboard


def get_gender_and_back_keyboard():
    gender_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    gender_keyboard.row(*[types.KeyboardButton(text=i) for i in cc.GENDER_LIST])
    gender_keyboard.add(types.KeyboardButton(text=cc.BACK))
    return gender_keyboard


def get_back_keyboard():
    back_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    back_keyboard.add(types.KeyboardButton(text=cc.BACK))
    return back_keyboard
