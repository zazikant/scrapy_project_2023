import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re

class BooksCrawlSpider(CrawlSpider):
    name = 'books_crawl'
    allowed_domains = ['truecadd.com']
    start_urls = ['https://www.truecadd.com']

    rules = (
        Rule(LinkExtractor(allow=r''), callback='parse_item', follow=True),
    )
    
    def parse_item(self, response):
        
        html = response.text
        
        body = response.xpath('//header[@class="clearfix"]//text()').getall()
    
        shody = response.xpath('//footer[@class="clearfix position-relative"]//text()').getall()
        for text in body:
            html = html.replace(text, '')
        for text in shody:
            html = html.replace(text, '')

        # Now, `html` contains the total response text without the elements matching the given xpath expressions
        #this is hemant comment
        
        email_found = False
        
        emails = re.findall(r'(?:concrete|Concrete)\s(?:Detailing|detailing)', html)
        for email in emails:
            if not email_found:
                yield {
                    'URL': response.url,
                    'Email': email
                }
                email_found = True
            else:
                break