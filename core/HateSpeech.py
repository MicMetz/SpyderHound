import scrapy
import pandas as pd



class HateSpeechSpider(scrapy.Spider):
    name = "hatespeech"
    train = []


    def parse(self, response):
        pass








if __name__ == "__main__":
    spider = HateSpeechSpider()
