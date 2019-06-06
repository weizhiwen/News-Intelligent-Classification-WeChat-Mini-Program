# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient
from scrapy import Item


class NewsSpiderPipeline(object):
    def process_item(self, item, spider):
        return item


class MongoDBPipeline(object):
    # 爬取之前调用，建立和MongoDB数据库的连接，方便后面使用
    def open_spider(self, spider):
        db_url = spider.settings.get('MONGODB_URI', 'mongodb:localhost:27017')
        db_name = spider.settings.get('MONGODB_DB_NAME', 'news')
        self.db_client = MongoClient(host='localhost:27017', username="weizhiwen", password="123456")
        self.db = self.db_client[db_name]

    # 爬取完全部数据之后调用，关闭与数据库的连接
    def close_spider(self, spider):
        self.db_client.close()

    # 处理爬取的每一项数据
    def process_item(self, item, spider):
        self.insert_db(item)
        return item

    # 具体的插入方法
    def insert_db(self, item):
        if isinstance(item, Item):
            item = dict(item)
        self.db.test_news.insert_one(item)
