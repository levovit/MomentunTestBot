from telebot import types


def get_setting_keyboard():
    settings_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    settings_keyboard.row(*[types.KeyboardButton(text=f"Change {i}") for i in ("age", "name", "gender")])
    settings_keyboard.add(types.KeyboardButton(text="Back"))
    return settings_keyboard


def get_menu_keyboard():
    menu_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    menu_keyboard.row(types.KeyboardButton(text="📖️ My information"), types.KeyboardButton(text="⚙️ settings"))
    return menu_keyboard


def get_gender_keyboard():
    gender_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    gender_keyboard.add(types.KeyboardButton(text="Male"))
    gender_keyboard.add(types.KeyboardButton(text="Female"))
    return gender_keyboard

