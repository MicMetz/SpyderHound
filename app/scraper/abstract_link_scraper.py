from abc import ABC, abstractmethod



class abstract_link_scraper(ABC):
    _parameters  = ""
    _quantity = 0
    _headers = ({'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.2403.157 Safari/537.36','Accept-Language': 'en-US, en;q=0.5'})
