import feedparser
url = 'http://feeds.reuters.com/news/wealth'
output = feedparser.parse(url)
from bs4 import BeautifulSoup
import requests


def parse_rss_data() :
    url_dict = {'Yahoo Finance'   : 'https://finance.yahoo.com/rss/',
                'Washington Post' : 'http://feeds.washingtonpost.com/rss/world',
                'Financial Times' : 'https://www.ft.com/?format=rss'
                }
    news_dict = {}
    yahoo_fin_dict = {}
    wash_post_dict = {}
    fin_times_dict = {}
    for url_name,url in url_dict.items():
        url = requests.get(url)
        soup = BeautifulSoup(url.content, 'xml')
        titles = soup.find_all('title')

        for ctr, title in enumerate(titles[2:]) :
            keyword = str(url_name) + '_' + str(ctr)
            if url_name == 'Yahoo Finance':
                yahoo_fin_dict[ctr] = {'title' : url_name, 'body' : title.text}
            if url_name == 'Washington Post':
                wash_post_dict[ctr] = {'title' : url_name, 'body' : title.text}
            if url_name == 'Financial Times':
                fin_times_dict[ctr] = {'title' : url_name, 'body' : title.text}

            # news_dict[keyword] = {'title' : url_name, 'body' : title.text}
    return yahoo_fin_dict,wash_post_dict,fin_times_dict

