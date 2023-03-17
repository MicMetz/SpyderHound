import threading
import urllib.request as urllibReq
from link_parser import LinkParser
from domain import get_domain_name
from main import *




class Spyder:
    """
        Cralwer class
        - Mutated Spider Based on the Python General Web Spider by Bucky Roberts <https://thenewboston.com/>
    """

    # Class variables
    _crawler_type = 'General'
    _project_name = ''
    _base_url = ''
    _domain_name = ''
    _queue_file = ''
    _crawled_file = ''
    _queue = set()
    _crawled = set()


    def __init__(self, project_name, base_url, domain_name):
        Spyder._project_name = project_name
        Spyder._base_url = base_url
        Spyder._domain_name = domain_name
        Spyder._queue_file = Spyder._project_name + '/_queue.txt'
        Spyder._crawled_file = Spyder._project_name + '/_crawled.txt'
        self.boot()
        self.crawl_page('First spider', Spyder._base_url)


    def boot(self):
        create_project_dir(Spyder._project_name)
        create_data_files(Spyder._project_name, Spyder._base_url)
        Spyder._queue = file_to_set(Spyder._queue_file)
        Spyder._crawled = file_to_set(Spyder._crawled_file)


    def crawl_page(self, thread_name, page_url):
        if page_url not in Spyder._crawled:
            print(thread_name + ' now crawling ' + page_url)
            print('Queue ' + str(len(Spyder._queue)) + ' | Crawled  ' + str(len(Spyder._crawled)))
            Spyder.add_links_to_queue(Spyder.gather_links(page_url))
            Spyder._queue.remove(page_url)
            Spyder._crawled.add(page_url)
            Spyder.update_files()


    def gather_links(self, page_url):
        html_string = ''
        try:
            response = urllibReq.urlopen(page_url)
            if 'text/html' in response.getheader('Content-Type'):
                html_bytes = response.read()
                html_string = html_bytes.decode("utf-8")
            finder = LinkParser(Spyder._base_url, page_url)
            finder.feed(html_string)
        except Exception as e:
            print(str(e))
            return set()
        return finder.page_links()

    def add_links_to_queue(self, links):
        for url in links:
            if (url in Spyder._queue) or (url in Spyder._crawled):
                continue
            if Spyder._domain_name != get_domain_name(url):
                continue
            Spyder._queue.add(url)

    def update_files(self):
        set_to_file(Spyder._queue, Spyder._queue_file)
        set_to_file(Spyder._crawled, Spyder._crawled_file)

    @property
    def crawled(self):
        return self._crawled

    @property
    def queue(self):
        return self._queue

    @property
    def queue_file(self):
        return self._queue_file

    @property
    def crawled_file(self):
        return self._crawled_file

    @property
    def crawler_type(self):
        return self._crawler_type

    @property
    def project_name(self):
        return self._project_name

    @property
    def base_url(self):
        return self._base_url

    @property
    def domain_name(self):
        return self._domain_name




class MultiThreadedSpyder(Spyder):
    def __init__(self, project_name, base_url, domain_name):
        super().__init__(project_name, base_url, domain_name)
        Spyder(project_name, base_url, domain_name)
        number_of_threads = 8
        _queue = file_to_set(Spyder._queue_file)
        if len(_queue) > 0:
            print(str(len(_queue)) + ' links in the _queue')
            for i in range(number_of_threads):
                t = threading.Thread(target=self.work)
                t.daemon = True
                t.start()
        self.crawl()

    def crawl(self):
        queued_links = file_to_set(Spyder._queue_file)
        if len(queued_links) > 0:
            print(str(len(queued_links)) + ' links in the _queue')
            self.update_files()

    def work(self):
        while True:
            url: str = Spyder._queue.pop()
            Spyder.crawl_page(threading.current_thread().name, url)

    def update_files(self):
        set_to_file(Spyder._queue, Spyder._queue_file)
        set_to_file(Spyder._crawled, Spyder._crawled_file)




class ChanSpyder(Spyder):
    def __init__(self, project_name, base_url, domain_name):
        super().__init__(project_name, base_url, domain_name)
        Spyder(project_name, base_url, domain_name)
        Spyder._crawler_type = 'Chan'
        self.crawl()

    def crawl(self):
        queued_links = file_to_set(Spyder._queue_file)
        if len(queued_links) > 0:
            print(str(len(queued_links)) + ' links in the _queue')
            self.update_files()

    def work(self):
        while True:
            url = Spyder._queue.pop()
            Spyder.crawl_page(threading.current_thread().name, url)

    def update_files(self):
        set_to_file(Spyder._queue, Spyder._queue_file)
        set_to_file(Spyder._crawled, Spyder._crawled_file)




class RedditSpyder(Spyder):
    def __init__(self, project_name, base_url, domain_name):
        super().__init__(project_name, base_url, domain_name)
        Spyder(project_name, base_url, domain_name)
        Spyder._crawler_type = 'Reddit'
        self.crawl()

    def crawl(self):
        queued_links = file_to_set(Spyder._queue_file)
        if len(queued_links) > 0:
            print(str(len(queued_links)) + ' links in the _queue')
            self.update_files()

    def work(self):
        while True:
            url = Spyder._queue.pop()
            Spyder.crawl_page(threading.current_thread().name, url)

    def update_files(self):
        set_to_file(Spyder._queue, Spyder._queue_file)
        set_to_file(Spyder._crawled, Spyder._crawled_file)
