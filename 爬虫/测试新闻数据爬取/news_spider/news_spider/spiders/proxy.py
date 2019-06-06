# 代理IP测试

import scrapy

class ProxySpider(scrapy.Spider):
    name = 'proxy'
    allowed_domains = []

    def start_requests(self):
        url = 'http://www.httpbin.org/get'
        for i in range(4):
            yield scrapy.Request(url=url, callback=self.parse, dont_filter=True)

    def parse(self,response):
        print(response.text)