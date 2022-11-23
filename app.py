from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    url = 'https://sanantonioreport.org/technology/?utm_source=googleads&utm_medium=search&utm_campaign=tribu'
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    # print(soup.prettify())
    newsAll = soup.find_all('div', class_='entry-wrapper',limit=7)
    #news = newsAll.a.text
    # # print(news)
    final = ""
    for news in newsAll:
        headLine = news.a.text
        final += "\u2022 "+headLine+"\n"
    #print(final)
    return render_template("index.html",News=final)
