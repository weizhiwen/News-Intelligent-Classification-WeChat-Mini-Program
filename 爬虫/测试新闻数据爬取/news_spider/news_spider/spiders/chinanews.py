# -*- coding: utf-8 -*-
from datetime import timedelta, datetime, date
import scrapy
from scrapy import Request
from ..items import ChinaNewsItem

# 要爬取的类别
crawl_category = ['国内', '国际', '军事', '体育', '社会', '娱乐', '财经']


# 格式化日期函数
def get_format_news_date(date=date.today()):
    start_date = datetime(date.year, date.month, date.day)
    # 返回格式化好的字符串
    return (start_date).strftime("%Y/%m%d")


# 中国新闻网爬取指定日期的新闻
class ChinanewsSpider(scrapy.Spider):
    name = 'chinanews'
    allowed_domains = ['www.chinanews.com']
    # 开始爬取的日期
    special_date = date.today()
    # 要爬取的天数
    special_days = 10
    # 直接构建出第一天的url
    start_urls = ['http://www.chinanews.com/scroll-news/{}/news.shtml'.format(get_format_news_date(special_date))]

    # 新闻列表解析方法
    def parse(self, response):
        for sel in response.css('div.content_list li'):
            category = sel.css('div.dd_lm>a::text').extract_first()
            # 如果该新闻类别在要爬取的类别名单内
            if category in crawl_category:
                china_news_item = ChinaNewsItem()
                china_news_item['news_title'] = sel.css('div.dd_bt>a::text').extract_first()
                china_news_item['news_url'] = 'http://www.chinanews.com' + sel.css('div.dd_bt>a::attr(href)').extract_first()
                china_news_item['news_datetime'] = str(ChinanewsSpider.special_date) + ' ' + sel.css('div.dd_time::text').extract_first().split(' ')[1]
                china_news_item['news_source'] = '中国新闻网'
                china_news_item['news_web_category'] = category
                china_news_item['news_machine_category'] = ''
                yield china_news_item
        # 构建上一天的新闻 url，注意这里的天数要先减去一天
        if ChinanewsSpider.special_days-1:
            ChinanewsSpider.special_days -= 1
            # 下一个要爬取的url
            next_date = ChinanewsSpider.special_date + timedelta(days=-1)
            ChinanewsSpider.special_date = next_date
            url = 'http://www.chinanews.com/scroll-news/{}/news.shtml'.format(get_format_news_date(next_date))
            yield Request(url, callback=self.parse)
