import telebot

bot = telebot.TeleBot('5850729460:AAFfq4RanAml5R9IZkNYFYjPFXyYScLBdaM')

@bot.message_handler(commands=['check'])
def check_subscription(message):
    chat_id = message.chat.id
    channel_username = 'yourai' # замените на имя канала для проверки
    subscribed = bot.get_chat_member(chat_id, chat_id).status == 'member'

    if subscribed:
        message_text = f'Вы подписаны на канал {channel_username}.'
    else:
        message_text = f'Вы не подписаны на канал {channel_username}.'

    bot.send_message(chat_id, message_text)

# bot.polling()



@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id,
                         "Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    else:
        bot.send_message(message.from_user.id,
                         "Я тебя не понимаю. Напиши /help.")


bot.polling(none_stop=True, interval=0)