import re
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    CallbackContext,
    Updater,
    PicklePersistence,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackQueryHandler,
)

from cred import TOKEN
from text import *
from gametext import red, black, green 
from menu import menu_keyboard, key_menu_keyboard, game_menu_keyboard
from key_buttons import button, tele_button, game_button
import random



def start(update:  Update, context: CallbackContext):
    context.bot.send_sticker(
        chat_id=update.effective_chat.id,
        sticker='CAACAgIAAxkBAAEFPoRizBXe2qjqZQUlJbUTopUMR6VMmgACjhYAAvcayUvqMHys4N1qTCkE'
    )
    update.message.reply_text(
        'Добро пожаловать, {username}'.format(
            username=update.effective_user.first_name \
                if update.effective_user.first_name is not None \
                    else update.effective_user
        ),
        reply_markup=menu_keyboard()             
    )
def start_game(update:  Update, context: CallbackContext):
    context.bot.send_sticker(
        chat_id=update.effective_chat.id,
        sticker='CAACAgIAAxkBAAEFQR9izZFSTDoa5nAgbxvOHBwtN6FqIwACNQADWgw3FSGN4egNBGo2KQQ'
    )
    update.message.reply_text(
        'Добро пожаловать в Казино, {username}'.format(
            username=update.effective_user.first_name \
                if update.effective_user.first_name is not None \
                    else update.effective_user
        ),
        reply_markup=game_menu_keyboard()             
    )

def back_menu(update:  Update, context: CallbackContext):
    context.bot.send_sticker(
        chat_id=update.effective_chat.id,
        sticker='CAACAgIAAxkBAAEFPoRizBXe2qjqZQUlJbUTopUMR6VMmgACjhYAAvcayUvqMHys4N1qTCkE'
    )
    update.message.reply_text(
        'Вы вернулись',
        reply_markup=menu_keyboard()             
    )

def back_game_menu(update:  Update, context: CallbackContext):
    context.bot.send_sticker(
        chat_id=update.effective_chat.id,
        sticker='CAACAgIAAxkBAAEFPoRizBXe2qjqZQUlJbUTopUMR6VMmgACjhYAAvcayUvqMHys4N1qTCkE'
    )
    update.message.reply_text(
        'Вы вернулись',
        reply_markup=menu_keyboard()             
    )

def option_menu(update:  Update, context: CallbackContext):
     context.bot.send_sticker(
        chat_id=update.effective_chat.id,
        sticker='CAACAgIAAxkBAAEFPsRizDww_BvLbvHCBu_PGhl4ZEkQmwACRRMAAmmvyUuppUmQogXywykE',
        reply_markup=key_menu_keyboard()
    )


            
    
HAHA = r'(?=('+(button[0])+r'))'
FACT = r'(?=('+(button[1])+r'))'
HZ = r'(?=('+(button[2])+r'))'
OPTION = r'(?=('+(button[3])+r'))'

GAME = r'(?=('+(tele_button[0])+r'))'
KURS = r'(?=('+(tele_button[1])+r'))'
NEWS = r'(?=('+(tele_button[2])+r'))'
BACK = r'(?=('+(tele_button[3])+r'))'


RED = r'(?=('+(game_button[0])+r'))'
BLACK = r'(?=('+(game_button[1])+r'))'
GREEN = r'(?=('+(game_button[2])+r'))'
BACK_GAME = r'(?=('+(game_button[3])+r'))'

usd = f'🇱🇷USD - {kursy[0]}, \n🇷🇺RUB - {kursy[2]}, \n🇪🇺EUR - {kursy[1]}, \n🇰🇿KZ - {kursy[3]}'

def haha_menu(update: Update, context: CallbackContext):
    update.message.reply_text(random.choice(jokes)),

def facts_menu(update: Update, context: CallbackContext):
    update.message.reply_text(random.choice(facts)),

def quote_menu(update: Update, context: CallbackContext):
    update.message.reply_text(random.choice(quotes)),

def kurs_menu(update: Update, context: CallbackContext):
    update.message.reply_text(usd)

def news_menu(update: Update, context: CallbackContext):
    update.message.reply_text(random.choice(newsy)),

def green_menu(update: Update, context: CallbackContext):
    update.message.reply_text(random.choice(green)),

def red_menu(update: Update, context: CallbackContext):
    update.message.reply_text(random.choice(red)),

def black_menu(update: Update, context: CallbackContext):
    update.message.reply_text(random.choice(black)),



updater = Updater(TOKEN, persistence=PicklePersistence(filename='bot-data'))
updater.dispatcher.add_handler(CommandHandler('start',start))


updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(HAHA),
    haha_menu
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(FACT),
    facts_menu
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(HZ),
    quote_menu
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(OPTION),
    option_menu
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(KURS),
    kurs_menu
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(BACK),
    back_menu
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(BACK_GAME),
    back_game_menu
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(NEWS),
    news_menu
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(GAME),
    start_game
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(RED),
    red_menu,
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(BLACK),
    black_menu
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(GREEN),
    green_menu
))



updater.dispatcher.add_handler(CallbackQueryHandler(button))
updater.start_polling()
updater.idle()