import pickle

import jieba
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, VotingClassifier
from sklearn.externals import joblib
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import KFold, cross_val_score, GridSearchCV
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.utils import Bunch
from data import NewsData
from common import get_stop_words_list, category_dict

# 1、准备数据

# 获取中文停用词数组
stop_words_list = get_stop_words_list()

# 新闻分类数组，作为 Bunch 的 target_names
category_list = ['国内', '国际', '军事', '体育', '社会', '娱乐', '财经']
train_news_data = NewsData(db='news', collection='train_news')
# test_news_data = NewsData(db='news', collection='test_news')

# 训练新闻数组
news_num_dict = {
    '国内': 10000,
    '国际': 10000,
    '军事': 10000,
    '体育': 10000,
    '社会': 10000,
    '娱乐': 10000,
    '财经': 10000,
}
train_news = train_news_data.get_train_news()

# 构建新闻标题分词的数组和新闻对应的数字分类数组
train_data = []
test_data = []
train_target = []
test_target = []

for item in train_news:
    train_data.append(" ".join(jieba.cut(item['news_title'])))
    train_target.append(category_dict[item['news_category']])

# 构建训练集数据bunch和测试集数据bunch
train_bunch = Bunch(data=train_data, target=train_target, target_names=category_list, DESCR='新闻训练数据集')


# 2、评估算法

# 设置评估算法的基准
num_folds = 10
seed = 7
scoring = 'accuracy'


# 基本的分类算法模型
# models = {
# 'LR': LogisticRegression(penalty='l2', C=10, solver='sag', multi_class='auto', n_jobs=-1),  # n_jobs=-1
# 'SVM': SVC(), # 几次训练正确率都是 0，弃用此算法模型
# 'CART': DecisionTreeClassifier(),
# 'MNB': MultinomialNB(alpha=0.01),
# 'KNN': KNeighborsClassifier(n_jobs=2),
# }
#
# tf_transformer = TfidfVectorizer(smooth_idf=False, stop_words=stop_words_list)
# X_train_counts_tf = tf_transformer.fit_transform(train_bunch.data)
#
# # 比较算法
# results = []
# for key in models:
#     kfold = KFold(n_splits=num_folds, random_state=seed)
#     cv_results = cross_val_score(models[key], X_train_counts_tf, train_bunch.target, cv=kfold, scoring=scoring)
#     results.append(cv_results)
#     print('%s : %f (%f)' % (key, cv_results.mean(), cv_results.std()))

# results = []

# 算法正确率
# kfold = KFold(n_splits=num_folds, random_state=seed)
# cart = DecisionTreeClassifier()
# models = []
# model_logistic = LogisticRegression(penalty='l2', C=10, solver='sag', multi_class='auto', n_jobs=-1)
# models.append(('logistic', model_logistic))
# model_cart = DecisionTreeClassifier()
# models.append(('cart', model_logistic))
# model_svc = SVC()
# ensemble_model = VotingClassifier(estimators=models)
# cv_results = cross_val_score(ensemble_model, X_train_counts_tf, train_bunch.target, cv=kfold, scoring=scoring)
# print(cv_results)

# LR 算法调参
# 每个分类 10000 数据：LR : 0.580571 (0.174557)
# 每个分类 80000 数据：LR : 0.629282 (0.164184)
# param_grid = {}
# param_grid['C'] = [1, 5, 10, 15, 20, 30]
# model = LogisticRegression(penalty='l2', solver='sag', multi_class='auto', n_jobs=-1)
# kfold = KFold(n_splits=num_folds, random_state=seed)
# grid = GridSearchCV(estimator=model, param_grid=param_grid, scoring=scoring, cv=kfold)
# grid_result = grid.fit(X=X_train_counts_tf, y=train_bunch.target)
# print('最优: %s 使用 %s' %(grid_result.best_score_, grid_result.best_params_))


# MNB 算法调参
# 每个分类 50000 数据：MNB : 0.610083 (0.155375)
# 每个分类 80000 数据：MNB : 0.619243 (0.164287)
# 所有分类 150多万数据：MNB: 0.7617135523266223
# param_grid = {}
# param_grid['alpha'] = [0.001, 0.01, 0.1, 1.5]
# model = MultinomialNB()
# kfold = KFold(n_splits=num_folds, random_state=seed)
# grid = GridSearchCV(estimator=model, param_grid=param_grid, scoring=scoring, cv=kfold, n_jobs=-1)
# grid_result = grid.fit(X=X_train_counts_tf, y=train_bunch.target)
# print('最优: %s 使用 %s' %(grid_result.best_score_, grid_result.best_params_))

#
# model = LogisticRegression(penalty='l2', C=10, solver='sag', multi_class='auto', n_jobs=-1)
# model.fit(X_train_counts_tf, train_bunch.target)


# print(tf_transformer.vocabulary_)
#
# print(type(tf_transformer.idf_))
# X_test_counts = tf_transformer.transform(test_bunch.data)
# print(type(X_test_counts))
# print(X_test_counts)
# predictions = model.predict(X_test_counts)
# # print(predictions[0])
# print(accuracy_score(test_bunch.target, predictions))
# print(confusion_matrix(test_bunch.target, predictions))
# print(classification_report(test_bunch.target, predictions))

# 保存transformer
def save_transformer(bunch, vocabulary_path='transformer.word'):
    # 计算tf-idf值
    tf_transformer = TfidfVectorizer(smooth_idf=False, stop_words=stop_words_list)
    tf_transformer.fit_transform(train_bunch.data)
    with open(vocabulary_path, 'wb') as f:
        pickle.dump(tf_transformer, f)
        print('成功保存词汇表')


# 保存tf-idf
def save_tfidf(bunch, tfidf_path='transformer.tfidf'):
    # 计算tf-idf值
    tf_transformer = TfidfVectorizer(smooth_idf=False, stop_words=stop_words_list)
    X_train_counts_tf = tf_transformer.fit_transform(bunch.data)
    with open(tfidf_path, 'wb') as f:
        pickle.dump(X_train_counts_tf, f)
        print('成功保存TF-IDF值')


# 保存transformer和TF-IDF值
def save_transformer_tfidf(bunch, vocabulary_path='transformer.word', tfidf_path='transformer.tfidf'):
    tf_transformer = TfidfVectorizer(smooth_idf=False, stop_words=stop_words_list)
    X_train_counts_tf = tf_transformer.fit_transform(bunch.data)
    with open(vocabulary_path, 'wb') as f:
        pickle.dump(tf_transformer, f)
        print('成功保存词汇表')
    with open(tfidf_path, 'wb') as f:
        pickle.dump(X_train_counts_tf, f)
        print('成功保存TF-IDF值')


# 分类算法生成模型
def classify_model(bunch, algorithm_model, tfidf_path, model_path):
    # 计算tf-idf值
    # tf_transformer = TfidfVectorizer(smooth_idf=False, stop_words=stop_words_list)
    # X_train_counts_tf = tf_transformer.fit_transform(train_bunch.data)
    # 读取TF-IDF值
    with open(tfidf_path, 'rb') as f:
        X_train_counts_tf = pickle.load(f)
    # 算法模型拟合
    print('算法模型拟合中...')
    algorithm_model.fit(X_train_counts_tf, bunch.target)
    # 保存模型信息
    with open(model_path, 'wb') as f:
        joblib.dump(algorithm_model, f, compress=1)
        print('成功生成' + model_path + '模型')


if __name__ == '__main__':
    # 生成TF-IDF值，只有当本地没有tfidf和有新数据时才执行该语句
    # save_transformer_tfidf(bunch=train_bunch)
    # 生成LR分类算法模型
    # model = LogisticRegression(penalty='l2', C=10, solver='sag', multi_class='auto', n_jobs=-1)
    # classify_model(train_bunch, model, 'transformer.tfidf', 'lr.model')
    # 生成MNB分类算法模型
    model = MultinomialNB(alpha=0.01)
    classify_model(train_bunch, model, 'transformer.tfidf', 'mnb.model')
