class NewsContent:
    def __init__(self, headlines: list):
        self.headlines = headlines

    def add_headline(self, title: str, url: str):
        """Adds a new content item with a headline and URL."""
        self.headlines.append({"headline": title, "url": url})