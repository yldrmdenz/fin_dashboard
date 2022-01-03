import feedparser
from bs4 import BeautifulSoup
import requests

def get_currency_rates():
    url_live = 'https://tr.investing.com/currencies/streaming-forex-rates-majors?__cf_chl_jschl_tk__=WtRCVITDhwpWy6kz53UYD.Q9bLWkW9oQvOzv5LEQULY-1641224699-0-gaNycGzND6U'
    requests.get(url_live)
def parse_rss_data() :
    url_dict = {'Yahoo Finance'   : 'https://finance.yahoo.com/rss/',
                'Washington Post' : 'http://feeds.washingtonpost.com/rss/world',
                'Financial Times' : 'https://www.ft.com/?format=rss'
                }
    yahoo_fin_dict = {}
    wash_post_dict = {}
    fin_times_dict = {}
    for url_name,url in url_dict.items():
        url = requests.get(url)
        soup = BeautifulSoup(url.content, 'xml')
        titles = soup.find_all('title')

        for ctr, title in enumerate(titles[2:]) :
            if url_name == 'Yahoo Finance':
                yahoo_fin_dict[ctr] = {'title' : url_name, 'body' : title.text}
            if url_name == 'Washington Post':
                wash_post_dict[ctr] = {'title' : url_name, 'body' : title.text}
            if url_name == 'Financial Times':
                fin_times_dict[ctr] = {'title' : url_name, 'body' : title.text}

            # news_dict[keyword] = {'title' : url_name, 'body' : title.text}
    return yahoo_fin_dict,wash_post_dict,fin_times_dict

