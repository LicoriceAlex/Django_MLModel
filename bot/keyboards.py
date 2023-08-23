from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
button_ask = KeyboardButton(text='Ask a question')
main_menu_keyboard.add(button_ask)

back_to_the_main_menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
button_back = KeyboardButton(text='Back to the main menu')
back_to_the_main_menu_keyboard.add(button_back)
