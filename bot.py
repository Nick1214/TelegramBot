import telebot
from StopGameParser import parse_stopgame
from RBKparser import get_news_rbc

token = "1932269741:AAHmk1twGN9NtInA7ivNPesVXggSlF8nh6c"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start", "help"])  # Нужен командный префикс, а text заменить на start !!!
def start_help_command(message):
    bot.send_message(message.from_user.id, "Введите /stopgame чтобы получить новости игр с сайта"
                                           "stopgame.ru")
    bot.send_message(message.from_user.id, "Введите /rbc, чтобы получить новости с сайта rbc.ru")


@bot.message_handler(commands=["stopgame"])
def stop_game_ru(message):
    array_with_news = parse_stopgame()
    for item in array_with_news:
        bot.send_message(message.from_user.id, item)


@bot.message_handler(commands=["rbc"])
def get_rbc_news(message):
    news = get_news_rbc()
    for item in news:
        bot.send_message(message.from_user.id, item)


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)