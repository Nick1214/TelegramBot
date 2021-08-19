from aiogram import Bot, Dispatcher, executor, types
from Bot import config
import requests
from bs4 import BeautifulSoup

bot = Bot(token=config.token)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start", "help"])
async def start_help_command(message: types.Message):
    await message.answer("This bot gives 20 last news from stopgame.ru game web-site")
    await message.answer("Use /news to start bot")


@dp.message_handler(commands="news")
async def get_news(message: types.Message):
    await message.answer("Последние 20 новостей с сайта: ")
    r = requests.get(url="https://stopgame.ru/news")
    array = []
    soup = BeautifulSoup(r.text, "lxml")
    main_card = soup.find("div", class_="tiles tiles-details").find("div", class_="items").find_all("div",
                                                                                                    class_="item article-summary")
    for card in main_card:
        card_href = card.find("a").get("href")
        array.append("https://stopgame.ru" + card_href)
    for item in array:
        await message.answer(item)

@dp.message_handler(commands="get_cs_news")
async def get_cs_news(message: types.Message):
    await message.answer("Last counter-strike news:")
    response = requests.get(url="https://www.cybersport.ru/counter-strike-go")
    array_with_news = []
    soup = BeautifulSoup(response.text, "lxml")
    all_cards = soup.find("article",
                          class_="materials-page grid grid--max-extra materials-page--disciplines").find(
        "div", class_="grid__col--ipad-4 grid__col--phone-6 margin-bottom--20"
    )
    for card in all_cards:
        card_href = card.find("div").find("h3").find("a").get("href")
        array_with_news.append(card_href)
    print()


if __name__ == '__main__':
    executor.start_polling(dp)