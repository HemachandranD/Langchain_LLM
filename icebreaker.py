from agents.news_lookup_agent import lookup


def icebreaker():
    news_url = lookup("bbc-news")
    return news_url


if __name__ == "__main__":
    output = icebreaker()
    print(output)
