import COVID19Py
import telebot
from telebot import types

covid19 = COVID19Py.COVID19()
bot = telebot.TeleBot('1450888366:AAEULd21zV4RtuX5WVe8X8W6wvye5Z62sLE')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('Во всем мире')
    btn2 = types.KeyboardButton('США')
    btn3 = types.KeyboardButton('Украина')
    markup.add(btn1, btn2, btn3)
    send_mess = f"<b>Привет {message.from_user.first_name}!</b>\nВведите страну"
    bot.send_message(message.chat.id, send_mess, parse_mode="html", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def mess(message):
    final_message = ""
    get_message_bot = message.text.strip().lower()
    if get_message_bot == "сша":
        location = covid19.getLocationByCountryCode("US")
    elif get_message_bot == "украина":
        location = covid19.getLocationByCountryCode("UA")
    else:
        location = covid19.getLatest()
        final_message = f"<u>Данные по всему миру:</u>\n<b>Забоелвшие:</b>{location['confirmed']}\n<b>Выздоровевших:</b>{location['recovered']}"

    if final_message == "":
        date = location[0]['last_updated'].split("T")
        time = date[1].split(".")
        print(location)
        final_message = f"<u>Данные по стране:</u>\n<b>Население:</b> {location[0]['country_population']}\n" \
                        f"<u>Последние обновление:</u>{date[0]} {time[0]}\n Последние данные: \n <b>Заболевшиx</b> {location[0]['latest']['confirmed']}\n" \
                        f"<b>Умерло:</b>{location[0]['latest']['deaths']}\n" \
                        f"<b>Выздоровело:</b>{location[0]['latest']['recovered']}"

    bot.send_message(message.chat.id, final_message, parse_mode="html")


bot.polling(none_stop=True)

# latest = covid19.getLatest()
# location = covid19.getLocationByCountryCode("UA")
#
# print(latest)
