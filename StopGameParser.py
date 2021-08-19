import requests
from bs4 import BeautifulSoup
import lxml

def parse_stopgame():
    r = requests.get(url="https://stopgame.ru/news")
    array = []
    soup = BeautifulSoup(r.text, "lxml")
    main_card = soup.find("div", class_="tiles tiles-details").find("div", class_="items").find_all("div",
                                                                                                        class_="item article-summary")
    for card in main_card:
        card_href = card.find("a").get("href")
        array.append("https://stopgame.ru" + card_href)
    return array

parse_stopgame()

class MyCar:
    def __init__(self, mark):
        self.mark = mark

    def get_mark(self):
        return self.mark
