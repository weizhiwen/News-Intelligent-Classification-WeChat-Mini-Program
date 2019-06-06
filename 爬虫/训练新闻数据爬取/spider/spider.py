# 爬取说明：
#   目标网站：
#       中国新闻网：http://www.chinanews.com
#   爬取规则：
#        http://域名/scroll-news/年/月日/news.shtml
#       例如，爬取2018年1月7日的新闻；http://www.chinanews.com/scroll-news/2018/0107/news.shtml
#   爬取字段：
#       新闻标题
#       新闻分类
from datetime import datetime, timedelta, date
from pymongo import MongoClient
import requests
from bs4 import BeautifulSoup
from random import randint
import time

# from .pc_user_agent import get_random


# 封装自己的MongoDB类
class MongoDB:
    # 构造方法
    def __init__(self, host, port, username, password, db, collection):
        self.host = host
        self.port = port
        self.client = MongoClient(host=host, port=port, username=username, password=password)
        self.db = self.client[db]
        self.collection = self.db[collection]

    # 批量插入方法
    def batch_add(self, dict):
        return self.collection.insert_many(dict)


# 构建mongoDB对象
mongoDB = MongoDB("localhost", 27017, "weizhiwen", "123456", "news", "train_news")


# 格式化日期函数，start_date 为开始日期，days 为倒推的天数
def format_news_date(start_date, days=0):
    return (start_date + timedelta(days=days)).strftime("%Y/%m%d")


# 爬取一天的新闻数据，每次爬取都使用不同的浏览器标识头
def crawl_data_by_url(url):
    r = requests.get(url, headers={"User-Agent": get_random()})
    r.encoding = "gb2312"
    soup = BeautifulSoup(r.text, "lxml")
    lis = soup.find(class_="content_list").find_all("li")
    list = []
    # 将每条新闻添加到list数组中
    for li in lis:
        try:
            # 新闻标题
            news_title = li.find("div", class_="dd_bt").find("a").get_text()
            # 新闻分类
            news_category = li.find(class_="dd_lm").find("a").get_text()
            # 构建新闻document数据
            news_document = {"news_category": news_category, "news_title": news_title}
            list.append(news_document)
        except:
            pass
    return list


# 爬虫爬取方法，start_date 为开始日期，days 为要爬取的天数
def spider_crawl(start_date, days):
    # 爬取每天的新闻
    for i in range(0, days):
        print("爬取", format_news_date(start_date, -i), "的新闻")
        # 根据中国新闻网新闻的规则构建url
        url = "http://www.chinanews.com/scroll-news/" + format_news_date(start_date, -i) + "/news.shtml"
        # 向mongoDB中批量插入数据
        list = crawl_data_by_url(url)
        mongoDB.batch_add(list)
        # 每爬完一天的数据就休息一下，防止被抓
        sleep_time = randint(5, 10)
        print("休息", sleep_time, "秒钟")
        time.sleep(sleep_time)
    print("爬取完毕！！！")

# 爬虫爬取军事分类下的新闻
def spider_crawl_mil(start_date, days):
    # 爬取每天的新闻
    for i in range(0, days):
        print("爬取", format_news_date(start_date, -i), "的新闻")
        # 根据中国新闻网新闻的规则构建url
        url = "http://www.chinanews.com/scroll-news/mil/" + format_news_date(start_date, -i) + "/news.shtml"
        # 判断list是否为空
        list = crawl_data_by_url(url)
        if len(list) > 0:
            # 如果list不为空，向mongoDB中批量插入数据
            mongoDB.batch_add(list)
            # 每爬完一天的数据就休息一下，防止被抓
            sleep_time = randint(5, 10)
            print("休息", sleep_time, "秒钟")
            time.sleep(sleep_time)
    print("爬取完毕！！！")


if __name__ == "__main__":
    # 爬取的开始日期，现已爬取 2019.03.06-2012.12.07 的数据，共 3035803 条数据
    start_date = datetime(2013, 12, 5)
    print(type(start_date))
    print((start_date + timedelta(days=-1)).date())
    # spider_crawl(start_date, 365)
    # print(date.today())
    # print(format_news_date(date.today()))
    # special_date = datetime(2018, 12, 7)
    # print('http://www.chinanews.com/scroll-news/{}/news.shtml'.format(format_news_date(special_date)))
    # print(datetime(2013, 12, 5).date())
    today = date.today()
    print('today', today)
    print(type(today))
    print(datetime(today.year, today.month, today.day).date())
    print(type(format_news_date(datetime(today.year, today.month, today.day))))
