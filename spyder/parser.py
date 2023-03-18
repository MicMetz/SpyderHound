from html.parser import HTMLParser
from urllib import parse


class Parser(HTMLParser):
    """
        Crawler Link Parsing Helper Functions
     - Based on the universial web crawler by Bucky Roberts <https://thenewboston.com/>
    """

    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'href' or attribute == 'src':
                    url = parse.urljoin(self.base_url, value)
                    self.links.add(url)

    def page_links(self):
        return self.links

    def error(self, message):
        pass

    def parse(self, html):
        self.feed(html)
        return self.links
