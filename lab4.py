import telebot

token = '7819849414:AAFftCY3FrQWN2N5I0qVR6lyaSibowmFKgs'
bot = telebot.TeleBot(token)
@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.reply_to(message, message.text)
if __name__ == '__main__':
     bot.infinity_polling()


