import telebot
from keyboards.inline import keyboards as inline_keyboards

BOT_TOKEN = '6545568971:AAHZY3fIUltUANghsPWik8CMvNubYRbgNjY'
bot = telebot.TeleBot(BOT_TOKEN)
@bot.message_handler(commands=['dog'])
def dog(message: telebot.types.Message):
    bot.send_photo(message.chat.id,'https://w.forfun.com/fetch/bc/bc45d1305c40e2ec7d72c71080b34751.jpeg')

@bot.message_handler(commands=['link'])
def link(messsage: telebot.types.Message):
    markup=inline_keyboards.git_hub()
    bot.send_message(messsage.chat.id, text='link', reply_markup=markup)

@bot.message_handler(commands=['balance'])
def balance(messsage: telebot.types.Message):
    markup=inline_keyboards.balance_inline()
    bot.send_message(messsage.chat.id, text='balance',reply_markup=markup)



bot.polling()