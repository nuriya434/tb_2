from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

def git_hub():
    markup = InlineKeyboardMarkup()
    button_link=InlineKeyboardButton(text='link_to_github', url='https://github.com')
    markup.add(button_link)
    return markup


def balance_inline():
    markup = InlineKeyboardMarkup()

    show_button=InlineKeyboardButton(text='show', callback_data='show')
    add_button=InlineKeyboardButton(text='add', callback_data='add')

    markup.add(show_button, add_button)

    return markup