import telegram
from key_buttons import button, tele_button, game_button

def menu_keyboard():
    keyboard = ([
    [telegram.KeyboardButton(button[0]),],
    [telegram.KeyboardButton(button[1]),
    telegram.KeyboardButton(button[2]),],
    [telegram.KeyboardButton(button[3]),],
    ])
    return telegram.ReplyKeyboardMarkup(
        keyboard, resize_keyboard=True, one_time_keyboard=False
    )

def key_menu_keyboard():
    keyboard = ([
    [telegram.KeyboardButton(tele_button[0]),],
    [telegram.KeyboardButton(tele_button[1]),
    telegram.KeyboardButton(tele_button[2]),], 
    [telegram.KeyboardButton(tele_button[3]),], 
    ])
    return telegram.ReplyKeyboardMarkup(
        keyboard, resize_keyboard=True, one_time_keyboard=False
    )

def game_menu_keyboard():
    keyboard = ([
    [telegram.KeyboardButton(game_button[0]),],
    [telegram.KeyboardButton(game_button[1]),
    telegram.KeyboardButton(game_button[2]),], 
    [telegram.KeyboardButton(game_button[3]),],
    ])
    return telegram.ReplyKeyboardMarkup(
        keyboard, resize_keyboard=True, one_time_keyboard=False
    )




