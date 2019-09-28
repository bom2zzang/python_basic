

from bs4 import BeautifulSoup
import urllib.request as req
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = "https://news.naver.com/"
res = req.urlopen(url)

soup = BeautifulSoup(res, 'html.parser')

head = soup.select("#today_main_news > div.hdline_news > ul > li > div.hdline_article_tit > a")

for a in head:
    print(a.string)


