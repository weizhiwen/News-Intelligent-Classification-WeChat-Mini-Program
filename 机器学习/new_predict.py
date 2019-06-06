# 加载模型文件，生成模型对象
import pickle
import scipy.sparse as sp
from pprint import pprint
import jieba
from sklearn.externals import joblib
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer, TfidfTransformer
from common import get_stop_words_list, category_dict_reverse
from data import NewsData

# 获取中文停用词数组
stop_words_list = get_stop_words_list()


# test_news = test_news_data.collection.find({'news_web_category': '社会'}).limit(1729)

# 加载词汇表
# vocabulary_file = 'vocabulary.word'
# with open(vocabulary_file, 'rb') as f:
#     train_transformer = pickle.load(f)
#     # count_vector = CountVectorizer(stop_words=stop_words_list, vocabulary=train_transformer.vocabulary_)
#
#     tf_transformer = TfidfVectorizer(smooth_idf=True, stop_words=stop_words_list,
#                                      vocabulary=train_transformer.vocabulary_)
#     tf_transformer._tfidf._idf_diag = sp.spdiags(train_transformer.idf_, diags=0, m=len(train_transformer.idf_),
#                                                  n=len(train_transformer.idf_))

# 对数据做一些处理
# test_data = []
# for item in test_news:
#     test_data.append(" ".join(jieba.cut(item['news_title'])))
# data = tf_transformer.transform(test_data)


# data = count_vector.transform(test_data)
# print(type(data))
# print(data)

# 使用加载生成的模型预测新样本
# model_file = 'lr.model'
# with open(model_file, 'rb') as f:
#     new_model = joblib.load(f)
#     predictions = new_model.predict(data)
#     category_list = predictions.tolist()
#     count = 0
#     news_category_list = []
#     for item in category_list:
#         category = category_dict_reverse[item]
#         news_category_list.append(category)
#         if category == '社会':
#             count += 1
#     print('社会新闻预测的正确率', count / 1729)
#     print(news_category_list)


# 新闻标题文本转文本矩阵
def text2matrix(text_list, transfomer_path='transformer'):
    # 加载词汇表
    with open(transfomer_path, 'rb') as f:
        train_transformer = pickle.load(f)
        tf_transformer = TfidfVectorizer(smooth_idf=True, stop_words=stop_words_list,
                                         vocabulary=train_transformer.vocabulary_)
        tf_transformer._tfidf._idf_diag = sp.spdiags(train_transformer.idf_, diags=0, m=len(train_transformer.idf_),
                                                     n=len(train_transformer.idf_))
    text_data = []
    for text in text_list:
        text_data.append(" ".join(jieba.cut(text)))
    return tf_transformer.transform(text_data)


# 分类模型预测
def classfiy_predict(model_path, data):
    with open(model_path, 'rb') as f:
        new_model = joblib.load(f)
        predictions = new_model.predict(data)
        category_list = predictions.tolist()
        news_category_list = []
        for item in category_list:
            category = category_dict_reverse[item]
            news_category_list.append(category)
        return news_category_list


if __name__ == '__main__':
    # 新闻单独测试
    # text = [
    #     '首战告负火箭此轮翻盘无望？ 杰弗森：系列赛已经结束',
    #     '约基奇已成系列赛最大无解杀器 享受MVP呼声他理所当然',
    #     '贾乃亮金晨再次否认恋情，晒完手机壳再晒猫节奏都一致',
    #     '余远帆被扔鸡蛋，于浩然被后援会坑，粉丝后援会有毒？',
    #     '再曝“黑料”！波音向全世界隐瞒了737MAX这一“致命问题”',
    #     '美舰开识别系统高调过台海 耍新花招刷存在感',
    #     '赶紧自查手机！三大运营商给你发送的这条短信，背后没那么简单',
    #     '新京报：药品价格放开后，“平价救命药”为何还短缺',
    #     '人民日报连续刊登：微观察·习近平主席的这一周',
    #     '16省份GDP增速跑赢全国6.4%增速 地方经济增速谁最快？',
    #     '客流高峰男子欲在武汉站跳楼 铁警这招亮了'
    # ]
    # data = text2matrix(text)
    # news_category_list = classfiy_predict(model_path='mn'
    #                                                  'b.model', data=data)
    # for i in range(len(text)):
    #     print('新闻标题：' + text[i] + '，预测分类：' + news_category_list[i])

    # 对数据库中没有进行机器分类的新闻进行测试
    test_news = NewsData(db='news', collection='test_news')
    # 查询所有 news_machine_category 不为空
    news_data = list(test_news.collection.find({"news_machine_category": {"$in": ['']}}))
    news_title_list = []
    for item in news_data:
        news_title_list.append(item['news_title'])
    data = text2matrix(news_title_list)
    news_category_list = classfiy_predict(model_path='mnb.model', data=data)
    # 总数据量
    total_count = len(news_data)
    # 预测正确的数量
    predict_true_count = 0
    for i in range(len(news_category_list)):
        if news_category_list[i] == news_data[i]['news_web_category']:
            predict_true_count += 1
        print(
            '预测分类: ' + news_category_list[i] + ', 实际分类: ' + news_data[i]['news_web_category'] + ', ' + news_title_list[
                i])
        # 更新数据库的机器分类字段
        test_news.collection.update_many({'news_title': news_title_list[i]},
                                    {'$set': {'news_machine_category': news_category_list[i]}})
    print('预测正确率: ' + str(predict_true_count / total_count))
