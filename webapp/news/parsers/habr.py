from datetime import datetime, timedelta
import locale
import platform

from bs4 import BeautifulSoup

from webapp.news.parsers.utils import get_html, save_news

if platform.system() == 'Windows':
    locale.setlocale(locale.LC_ALL, "russia")
else:
    locale.setlocale(locale.LC_TIME, 'ru_RU.utf8')


def parse_habr_date(date_str):
    if 'сенодня' in date_str:
        today = datetime.now()
        date_str = date_str.replace('сегодня', today.strftime('%d %B %Y'))
    elif 'вчера' in date_str:
        yesterday = datetime.now() - timedelta(days=1)
        date_str = date_str.replace('вчера', yesterday.strftime('%d %B %Y'))
    try:
        return datetime.strptime(date_str, '%d %B %Y в %H:%M')
    except ValueError:
        return datetime.now()


def get_habr_snippets():
    html = get_html('https://habr.com/ru/search/?q=python&target_type=posts&order=date')
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        all_news = soup.find('div', class_='tm-articles-list').find_all('article', class_ = 'tm-articles-list__item')
        for news in all_news:
            title = news.find('a', class_='tm-article-snippet__title-link').text
            url = news.find('a', class_='tm-article-snippet__title-link')['href']
            url = 'https://habr.com' + url
            published = news.find('span', class_='tm-article-snippet__datetime-published').text
            published = parse_habr_date(published)
            save_news(title, url, published)