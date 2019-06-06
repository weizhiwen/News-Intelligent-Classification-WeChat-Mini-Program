from flask import Flask, request

from new_predict import text2matrix, classfiy_predict
from util.mongo import MongoDB
from util.result import Result, PageResult
import re

app = Flask(__name__)

mongo = MongoDB(db='news', collection='test_news', username='weizhiwen', password='123456')


@app.route('/')
def hello_world():
    return '基于Scrapy的智能分类微信小程序后端API'


# 新闻列表
@app.route('/news/<int:offset>/<int:limit>')
def news(offset, limit=20):
    result = {}
    items = []
    category = request.args.get('category')
    keyword = request.args.get('keyword')
    if offset < 0 or limit <= 0:
        result = Result(code=Result.FAIL, msg='offset或limit参数有误！')
        return result.to_json()
    # 筛选字段，过滤 _id(ObjectId) 避免序列化异常
    column = {'_id': 0}
    # 组装查询条件，无法拼接出带模糊查询的 sql，pymongo 就是个垃圾！！！
    # condition = {}
    # if category:
    #     condition['news_web_category'] = category
    # if keyword:
    #     regex = {'$regex': '.*{}.*'.format(keyword)}
    #     condition['new_title'] = regex
    # print(condition)
    try:
        if not category and not keyword:
            items = list(mongo.collection.find({}, column).sort('news_datetime', -1).skip(offset).limit(limit))
            count = mongo.collection.find({}, column).count()
            result = PageResult(items, count=count)
        if category and not keyword:
            items = list(mongo.collection.find({'news_web_category': category}, column).sort('news_datetime', -1).skip(
                offset).limit(limit))
            count = mongo.collection.find({'news_web_category': category}, column).count()
            result = PageResult(items, count=count)
        if not category and keyword:
            items = list(
                mongo.collection.find({'news_title': re.compile(keyword, re.IGNORECASE)}, column).sort('news_datetime',
                                                                                                       -1).skip(
                    offset).limit(limit))
            count = mongo.collection.find({'news_title': re.compile(keyword, re.IGNORECASE)}, column).count()
            result = PageResult(items, count=count)
        if keyword and category:
            items = list(
                mongo.collection.find({'news_web_category': category, 'news_title': re.compile(keyword, re.IGNORECASE)},
                                      column).sort('news_datetime', -1).skip(offset).limit(limit))
            count = mongo.collection.find(
                {'news_web_category': category, 'news_title': re.compile(keyword, re.IGNORECASE)}, column).count()
            result = PageResult(items, count=count)
    except Exception as e:
        result = Result(code=Result.FAIL, msg=e)
    return result.to_json()


# 新闻分类
@app.route('/news/<title>')
def category(title):
    news_title_list = []
    news_title_list.append(title)
    data = text2matrix(news_title_list)
    # 使用 MNB 分类模型对新闻进行分类
    news_category_list = classfiy_predict(model_path='mnb.model', data=data)
    return Result(items=news_category_list[0]).to_json()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
