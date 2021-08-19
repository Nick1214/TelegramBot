import requests
from bs4 import BeautifulSoup
import lxml


def make_request():
    r = requests.get(url="https://www.rbc.ru/")
    soup = BeautifulSoup(r.text, "lxml")
    return soup




def get_news_rbc():
    soup = make_request()
    all_news = soup.find("div", class_="main__list").find_all("div", class_="main__feed js-main-reload-item")
    array = []
    array_with_heading = []
    for news in all_news:
        news_href = news.find("a").get("href")
        news_heading = news.find("span", class_="main__feed__title")
        array_with_heading.append(news_heading.text)
        array.append(news_href)
    return array  # Must be returned
    # print(array_with_heading)  # Must be returned

#
# def get_currency():
#     soup = make_request()
#     all_values = soup.find("div", class_="l-col-right__inner").find(
#         "div", class_="indicators__wrap"
#     )
#     array = []
#     for value in all_values:
#         values_from_cb = value.find("a")
#         array.append(values_from_cb)
#     print(array)  # Must be returned
