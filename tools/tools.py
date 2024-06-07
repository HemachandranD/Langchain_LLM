import os
from dotenv import load_dotenv
from newsapi import NewsApiClient

load_dotenv()
NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")

# Init
newsapi = NewsApiClient(api_key=NEWSAPI_KEY)


def scrape_top_news(source):
    """Take the source as an input string. Scrape top news from bbc-news,
    returns the output as an string."""
    response = newsapi.get_top_headlines(sources=source)
    response = response["articles"][0]
    return response
