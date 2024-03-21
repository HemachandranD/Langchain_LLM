import os
from dotenv import load_dotenv
from newsapi import NewsApiClient

load_dotenv()
NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")

# Init
newsapi = NewsApiClient(api_key=NEWSAPI_KEY)


def scrape_top_news(source):
    """Scrape top news from bbc-news"""
    response = newsapi.get_top_headlines(sources=source)
    return response['articles'][0]