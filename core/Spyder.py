from bs4.element import ResultSet
import requests
from bs4 import BeautifulSoup
import re



class Spyder():
    url: str = None
    dom: str = None
    emails: set = None
    links: set = None
    images: set = None
    headings: set = None
    paragraphs: set = None
    page: str = None
    raw_text_words: str = None
    paragraphs_by_headings: dict = {}


    def __init__(self, url: str):
        self.url = url
        self.get_dom()

        soup = BeautifulSoup(self.dom, "html.parser")
        self.headings = soup.find_all(re.compile("^h[1-6]$"))
        self.raw_text_words = soup.get_text().split()
        self.emails = soup.find_all("a", href=re.compile("mailto:"))
        self.images = soup.find_all("img")
        self.paragraphs = soup.find_all("p")
        self.links = soup.find_all("a", href=re.compile("http"))
        self.paragraphs_by_headings = self.get_paragraphs_by_headings()
        self.page = soup.prettify()

        # self.headings = set(re.findall(r"<h[1-6]>(.*?)</h[1-6]>", self.dom))
        # self.emails = set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,3}", self.dom))
        # self.images = set(re.findall(r"<img.*?src=\"(.*?)\".*?>", self.dom))
        # self.paragraphs = set(re.findall(r"<p>(.*?)</p>", self.dom))
        # self.links = set(re.findall("'((http)s?://.*?)'", self.dom))
        # self.links = set(re.findall(r"(http|https)://[A-Za-z0-9./]+", self.dom))
        # self.paragraphs_by_headings = self.get_paragraphs_by_headings()



    def get_data(self) -> dict:
        return {
            "url": self.url,
            "dom": self.dom,
            "raw_text_words": self.raw_text_words,
            "emails": self.emails,
            "links": self.links,
            "images": self.images,
            "headings": self.headings,
            "paragraphs": self.paragraphs,
            "paragraphs_by_headings": self.paragraphs_by_headings
        }


    def get_headings(self) -> ResultSet:
        return self.headings


    def get_emails(self):
        return self.emails


    def get_images(self) -> ResultSet:
        return self.images


    def get_paragraphs(self) -> ResultSet:
        return self.paragraphs


    def get_paragraphs_by_headings(self) -> dict:
        return self.paragraphs_by_headings


    def get_links(self) -> ResultSet:
        return self.links


    def get_dom(self):
        print(f"URL: {self.url}")
        http_obj = requests.get(self.url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'})
        http_obj.raise_for_status()
        self.dom = http_obj.text


    def set_paragraphs_by_headings(self) -> dict:
        if self.headings is not None:
            headings = self.headings
        else:
            headings = self.get_headings()
        for heading in headings:
            self.paragraphs_by_headings[heading] = set(re.findall(r"<p>(.*?)</p>", self.dom))
        return self.paragraphs_by_headings


    def show_dom(self):
        print(self.dom)


    def show_headings(self):
        print(self.headings)


    def show_links(self):
        print(self.links)
    #
    # def list_email(self):
    #     self.emails = set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,3}", self.dom))
    #
    # def list_headings(self):
    #     self.dom = self.get_headings()
    #
    # def list_links(self):
    #     self.links = set(re.findall(r"(http|https)://[A-Za-z0-9./]+", self.dom))
    #
    # def list_images(self):
    #     self.images = set(re.findall(r"(http|https)://[A-Za-z0-9./].+?\.(jpg|png|gif)", self.dom))
    #
    # def list_paragraphs_by_headings(self):
    #     self.paragraphs_by_headings = {}
    #     if self.headings is not None:
    #         headings = self.headings
    #     else:
    #         headings = self.get_headings()
    #
    #     for heading in headings:
    #         self.paragraphs_by_headings[heading] = set(re.findall(r"<p>(.*?)</p>", self.dom))
    #
    # def list_paragraphs(self):
    #     self.paragraphs = set(re.findall(r"<p>(.*?)</p>", self.dom))
