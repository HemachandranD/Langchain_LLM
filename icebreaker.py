from agents.news_lookup_agent import lookup
from tools.tools import scrape_top_news


def icebreaker():
    news_url = lookup("bbc-news")
    return news_url


if __name__ == "__main__":
    print(icebreaker())
