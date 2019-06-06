# Scrapy 爬虫执行脚本
from scrapy import cmdline

cmdline.execute('scrapy crawl wangyi'.split())
cmdline.execute('scrapy crawl chinanews'.split())