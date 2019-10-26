import telebot

bot = telebot.TeleBot('904476426 :AAHh7Yrf5uEixLvJnM-GPcE27ndrnyNGZbM')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'sdfsdgdfhfgjfjhgj /start')

bot.polling()
