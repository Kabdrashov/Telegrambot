import requests
from datetime import datetime
import telebot
from auth_data import token


def get_data():
    req = requests.get("https://yobit.net/api/3/ticker/btc_usd")
    response = req.json()
    sell_price = response["btc_usd"]['sell']
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%m')}\nSell BTC price: {sell_price} ")


def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=["start"])
    def start_message(message):
        bot.send_message(message.chat.id, "Привет пиши 'price' для получение стоимости биткоина")


    @bot.message_handler(content_types=["text"])
    def send_text(message):
        if message.text.lower() == 'price':
            try:
                req = requests.get("https://yobit.net/api/3/ticker/btc_usd")
                response = req.json()
                sell_price = response["btc_usd"]['sell']
                bot.send_message(message.chat.id, f"{datetime.now().strftime('%Y-%m-%d %H:%m')}\nSell BTC price: {sell_price} ")
            except Exception as ex:
                print(ex)
                bot.send_message(message.chat.id, "Чувак что-то пошло не так")
        else:
            bot.send_message(message.chat.id, "Проверь что ты написал")

    bot.polling()

if __name__ == '__main__':
    #get_data()
    telegram_bot(token)