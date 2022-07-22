from urllib import request, error
from bs4 import BeautifulSoup
import random
joke = []
with request.urlopen('https://www.anekdot.ru/') as resp:
    data = resp.read()
    soup = BeautifulSoup(data, 'html.parser')
    items = soup.find_all('div', attrs={'class': 'text'})
    for item in items:
        text = item.get_text()
        joke.append(text)
        
jokes = joke

fact = []
with request.urlopen('https://europaplus.ru/news/samye-interesnye-fakty-obo-vsem-na-svete') as resp:
    data = resp.read()
    soup = BeautifulSoup(data, 'html.parser')
    items = soup.find_all('p', attrs={'class': 'typography typography_type_text typography_size_max typography_mark_light'})
    for item in items:
        text = item.get_text()
        fact.append(text)

facts = fact


quote = []
with request.urlopen('https://allcitations.ru/tema/citaty-so-smyslom') as resp:
    data = resp.read()
    soup = BeautifulSoup(data, 'html.parser')
    items = soup.find_all('div', attrs={'class': 'cittext'})
    for item in items:
        text = item.get_text()
        quote.append(text)

quotes = quote

kurs = []
with request.urlopen('https://www.cbk.kg/') as resp:
    data = resp.read()
    soup = BeautifulSoup(data, 'html.parser')
    items = soup.find_all('td', attrs={'class': 'sell'})
    for item in items:
        text = item.get_text()
        kurs.append(text)

kursy = kurs

news = []
with request.urlopen('https://akipress.org/?ysclid=l5i0kcl9r4823102097') as resp:
    data = resp.read()
    soup = BeautifulSoup(data, 'html.parser')
    items = soup.find_all('a', attrs={'class': 'newslink'})
    for item in items:
        text = item.get_text()
        news.append(text)

newsy = news








