from pymongo import MongoClient
from pprint import pprint


# 新闻数据类
class NewsData(object):
    # 构造方法，使用指定的db和collection
    def __init__(self, db, collection, host='127.0.0.1', port=27017, username='weizhiwen', password='123456'):
        self.client = MongoClient(host=host, port=port, username=username, password=password)
        self.db = self.client[db]
        self.collection = self.db[collection]

    # 获取训练数据库中的新闻数据
    def get_train_news(self, news_num_dict=None):
        new_list = []
        # 如果传入了各个分类指定的新闻数量，就使用指定值，否则查询所有
        if news_num_dict:
            new_list.extend(self.collection.find({'news_category': '国内'}).limit(news_num_dict['国内']))
            new_list.extend(self.collection.find({'news_category': '国际'}).limit(news_num_dict['国际']))
            new_list.extend(self.collection.find({'news_category': '军事'}).limit(news_num_dict['军事']))
            new_list.extend(self.collection.find({'news_category': '体育'}).limit(news_num_dict['体育']))
            new_list.extend(self.collection.find({'news_category': '社会'}).limit(news_num_dict['社会']))
            new_list.extend(self.collection.find({'news_category': '娱乐'}).limit(news_num_dict['娱乐']))
            new_list.extend(self.collection.find({'news_category': '财经'}).limit(news_num_dict['财经']))
        else:
            new_list.extend(self.collection.find({'news_category': {'$in': ['国内', '国际', '军事', '体育', '社会', '娱乐', '财经']}}))
        return new_list

    # 获取测试数据库中的新闻数据
    def get_test_news(self, news_num_dict=None):
        new_list = []
        # 如果传入了各个分类指定的新闻数量，就使用指定值，否则查询所有
        if news_num_dict:
            new_list.extend(self.collection.find({'news_web_category': '国内'}).limit(news_num_dict['国内']))
            new_list.extend(self.collection.find({'news_web_category': '国际'}).limit(news_num_dict['国际']))
            new_list.extend(self.collection.find({'news_web_category': '军事'}).limit(news_num_dict['军事']))
            new_list.extend(self.collection.find({'news_web_category': '体育'}).limit(news_num_dict['体育']))
            new_list.extend(self.collection.find({'news_web_category': '社会'}).limit(news_num_dict['社会']))
            new_list.extend(self.collection.find({'news_web_category': '娱乐'}).limit(news_num_dict['娱乐']))
            new_list.extend(self.collection.find({'news_web_category': '财经'}).limit(news_num_dict['财经']))
        else:
            new_list.extend(self.collection.find({'news_web_category': {'$in': ['国内', '国际', '军事', '体育', '社会', '娱乐', '财经']}}))
        return new_list


    # 分离训练数据集和评估数据集
    def get_train_and_test_news(self, test_size=0.33):
        news = self.get_news()
        total_num = len(news)
        # 前 (1-test_size) 的数据作为训练数据集
        size1 = int((1 - test_size) * total_num)
        train_news_list = news[:size1]
        # 后 test_size 的数据作为评估（测试）数据集
        size2 = - int(test_size * total_num)
        test_news_list = news[size2:]
        news_dict = {'train_news': train_news_list, 'test_news': test_news_list}
        return news_dict


if __name__ == '__main__':
    train_news_data = NewsData(db='news', collection='train_news')
    test_news_data = NewsData(db='news', collection='test_news')
    pprint(test_news_data.get_test_news())
    print(len(test_news_data.get_test_news()))
