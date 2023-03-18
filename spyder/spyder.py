import threading
import urllib.request as urllibReq
from parser import LinkParser
from domain import get_domain_name
from main import *
import sys
import logging
import inspect



class SpyderLogger(logging.Filter):
    def filter(self, record):
        # record.extract_line_num = line_num
        return True




class Spyder:
    """
        Cralwer class
        - Mutated Spider - Based on the universial web crawler by Bucky Roberts <https://thenewboston.com/>
    """

    def __init__(self, project_name, base_url, domain_name):
        self._project_name = project_name
        self._base_url = base_url
        self._domain_name = domain_name
        self._queue_file = self._project_name + '/_queue.txt'
        self._crawled_file = self._project_name + '/_crawled.txt'
        self._queue = ""
        self._crawled = ""
        self._crawler_type = 'General'
        self._crawler_purpose = 'Hate'
        self._domain_name = ''
        self._queue_file = ''
        self._crawled_file = ''
        self._queue = set()
        self._crawled = set()

        # ----------------LOGGER CONFIGURATION----------------#
        self.utils_logger = logging.getLogger('spyder-mod.utils')
        self.log_level = 'INFO'

        logger = logging.getLogger('spyder-mod')
        logger.setLevel(self.log_level)
        logger.addFilter(SpyderLogger())

        channel = logging.StreamHandler()
        channel.setLevel(self.log_level)

        formatter = logging.Formatter('%(asctime)s - %(name)-25s - %(filename)-15s - %(funcName)-20s - %(extract_line_num)-5s - %(levelname)-8s - %(message)s')
        channel.setFormatter(formatter)
        logger.addHandler(channel)

        if not self.utils_logger.hasHandlers():
            logger.addHandler(channel)

        self.crawl_page('First spider', self._base_url)


    @staticmethod
    def create_project_dir(directory):
        if not os.path.exists(directory):
            print('Creating directory ' + directory)
            os.makedirs(directory)


    @staticmethod
    def create_data_files(project_name, base_url):
        queue = os.path.join(project_name, '_queue.txt')
        crawled = os.path.join(project_name, "_crawled.txt")
        if not os.path.isfile(queue):
            Spyder.write_file(queue, base_url)
        if not os.path.isfile(crawled):
            Spyder.write_file(crawled, '')

    @staticmethod
    def write_file(path, data):
        with open(path, 'w') as f:
            f.write(data)

    @staticmethod
    def append_to_file(path, data):
        with open(path, 'a') as file:
            file.write(data + '\n')

    @staticmethod
    def delete_file_contents(path):
        with open(path, 'w'):
            pass

    @staticmethod
    def file_to_set(file_name):
        results = set()
        with open(file_name, 'rt') as f:
            for line in f:
                results.add(line.replace('\n', ''))
        return results



class ChanSpyder(Spyder):
    """
        4Chan | Kiwifarm Cralwer class
        -
    """

    def __init__(self, project_name, base_url, domain_name):
        super().__init__(project_name, base_url, domain_name)
        self._crawler_type = 'Chan'
        self._crawler_purpose = 'Hate'
        self._domain_name = domain_name
        self._queue_file = self._project_name + '/_queue.txt'
        self._crawled_file = self._project_name + '/_crawled.txt'
        self._queue = set()
        self._crawled = set()
        self.crawl_page('First spider', self._base_url)

    def crawl_page(self, thread_name, page_url):
        if page_url not in self._crawled:
            print(thread_name + ' now crawling ' + page_url)
            print('Queue ' + str(len(self._queue)) + ' | Crawled  ' + str(len(self._crawled)))
            self.add_links_to_queue(self.gather_links(page_url))
            self._queue.remove(page_url)
            self._crawled.add(page_url)
            self.update_files()

    def gather_links(self, page_url):
        html_string = ''
        try:
            response = urllibReq.urlopen(page_url)
            if 'text/html' in response.getheader('Content-Type'):
                html_bytes = response.read()
                html_string = html_bytes.decode("utf-8")
            finder = LinkParser(self._base_url, page_url)
            finder.feed(html_string)
        except Exception as e:
            print(str(e))
            return set()
        return finder.page_links()

    def add_links_to_queue(self, links):
        for url in links:
            if (url in self._queue) or (url in self._crawled):
                continue
            if self._domain_name != get_domain_name(url):
                continue
            self._queue.add(url)

    def update_files(self):
        if len(self._queue) > 0:
            self.write_file(self._queue_file, '\n'.join(self._queue))
            self._queue.clear()
        if len(self._crawled) > 0:
            self.write_file(self._crawled_file, '\n'.join(self._crawled))
            self._crawled.clear()


class ReddSpyder(Spyder):
    """
        Reddit Cralwer class
        -
    """

    def __init__(self, project_name, base_url, domain_name):
        super().__init__(project_name, base_url, domain_name)
        self._crawler_type = 'Reddit'
        self._crawler_purpose = 'Hate'
        self._domain_name = domain_name
        self._queue_file = self._project_name + '/_queue.txt'
        self._crawled_file = self._project_name + '/_crawled.txt'
        self._queue = set()
        self._crawled = set()
        self.crawl_page('First spider', self._base_url)

    def crawl_page(self, thread_name, page_url):
        if page_url not in self._crawled:
            print(thread_name + ' now crawling ' + page_url)
            print('Queue ' + str(len(self._queue)) + ' | Crawled  ' + str(len(self._crawled)))
            self.add_links_to_queue(self.gather_links(page_url))
            self._queue.remove(page_url)
            self._crawled.add(page_url)
            self.update_files()

    def gather_links(self, page_url):
        html_string = ''
        try:
            response = urllibReq.urlopen(page_url)
            if 'text/html' in response.getheader('Content-Type'):
                html_bytes = response.read()
                html_string = html_bytes.decode("utf-8")
            finder = LinkParser(self._base_url, page_url)
            finder.feed(html_string)
        except Exception as e:
            print(str(e))
            return set()
        return finder.page_links()

    def add_links_to_queue(self, links):
        for url in links:
            if (url in self._queue) or (url in self._crawled):
                continue
            if self._domain_name != get_domain_name(url):
                continue
            self._queue.add(url)

    def update_files(self):
        if len(self._queue) > 0:
            self.write_file(self._queue_file, '\n'.join(self._queue))
            self._queue.clear()
        if len(self._crawled) > 0:
            self.write_file(self._crawled_file, '\n'.join(self._crawled))
            self._crawled.clear()



class TwitSpyder(Spyder):
    """
        Twitter Cralwer class
        -
    """

    def __init__(self, project_name, base_url, domain_name):
        super().__init__(project_name, base_url, domain_name)
        self._crawler_type = 'Twitter'
        self._crawler_purpose = 'Hate'
        self._domain_name = domain_name
        self._queue_file = self._project_name + '/_queue.txt'
        self._crawled_file = self._project_name + '/_crawled.txt'
        self._queue = set()
        self._crawled = set()
        self.crawl_page('First spider', self._base_url)

    def crawl_page(self, thread_name, page_url):
        if page_url not in self._crawled:
            print(thread_name + ' now crawling ' + page_url)
            print('Queue ' + str(len(self._queue)) + ' | Crawled  ' + str(len(self._crawled)))
            self.add_links_to_queue(self.gather_links(page_url))
            self._queue.remove(page_url)
            self._crawled.add(page_url)
            self.update_files()

    def gather_links(self, page_url):
        html_string = ''
        try:
            response = urllibReq.urlopen(page_url)
            if 'text/html' in response.getheader('Content-Type'):
                html_bytes = response.read()
                html_string = html_bytes.decode("utf-8")
            finder = LinkParser(self._base_url, page_url)
            finder.feed(html_string)
        except Exception as e:
            print(str(e))
            return set()
        return finder.page_links()

    def add_links_to_queue(self, links):
        for url in links:
            if (url in self._queue) or (url in self._crawled):
                continue
            if self._domain_name != get_domain_name(url):
                continue
            self._queue.add(url)

    def update_files(self):
        if len(self._queue) > 0:
            self.write_file(self._queue_file, '\n'.join(self._queue))
            self._queue.clear()
        if len(self._crawled) > 0:
            self.write_file(self._crawled_file, '\n'.join(self._crawled))
            self._crawled.clear()
