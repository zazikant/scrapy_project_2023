import scrapy
import scraper_helper as sh


reviews_url = "https://www.amazon.in/product-reviews/{}"
asin_list = ['B0BHGVW38M']

class AbcSpider(scrapy.Spider):
    name = "ABC"

    def start_requests(self):
        for asin in asin_list:
            url = reviews_url.format(asin)
            yield scrapy.Request(url)

    def parse(self, response):
        print(' I am in parse')
