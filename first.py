import scrapy


class FirstSpider(scrapy.Spider):
    name = 'first'
    #allowed_domains = ['www.baidu.com']
    start_urls = ['https://www.bilibili.com/']

    def parse(self, response):
        pass
