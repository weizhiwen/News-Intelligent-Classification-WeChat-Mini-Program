# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class NewsSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

# 中国新闻网新闻实体类
class ChinaNewsItem(scrapy.Item):
    news_title = Field()  # 新闻标题
    news_url = Field()  # 新闻链接
    news_datetime = Field()  # 新闻日期时间
    news_source = Field()  # 新闻来源
    news_web_category = Field()  # 网站上新闻的分类
    news_machine_category = Field()  # 机器对新闻的分类
