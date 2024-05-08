import telebot
from congig import slovar, TOKEN
from Utils import APIException, CryptoConverter

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands = ['start', 'help'])
def start(message: telebot.types.Message):
    text = """Чтобы начать работу введите команду боту в следующем формате:\n<имя валюты> \
<в какую валюту перевести><количество переводимой валюты>\n<увидеть список всех доступных валют:/value""" 
    bot.reply_to(message, text)

@bot.message_handler(commands = ['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты'
    for i in slovar.keys():
        text = '\n'.join((text,i))
    bot.reply_to(message, text)

@bot.message_handler(content_types= ['text'])
def convert(message: telebot.types.Message):
    
    try:
        values = message.text.split(' ')
    
        if len(values) != 3:
            raise APIException('неверное количество параметров')
    
        quote, base, amount = values
        total_base = CryptoConverter.get_price(quote, base, amount)
    except APIException as e:
        bot.reply_to(message,f'Ошибка пользователя\n {e}')
    except Exception as e:
        bot.reply_to(message,f'Не удалось обработать команду\n {e}')
    else:
        text = f'Цена {amount} {quote} в {base} - {total_base}'
        bot.send_message(message.chat.id, text)


bot.polling()