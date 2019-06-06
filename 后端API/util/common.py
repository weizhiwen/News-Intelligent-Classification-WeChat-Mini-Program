# 获取停用词表数组
def get_stop_words_list():
    with open('stopwords.txt', encoding='utf-8', errors='ignore') as file:
        return file.read().replace('\n', ' ').split()


# 新闻分类文本转数字
category_dict = {
    '国内': 0,
    '国际': 1,
    '军事': 2,
    '体育': 3,
    '社会': 4,
    '娱乐': 5,
    '财经': 6
}

# 新闻分类数字转文本
category_dict_reverse = {
    0: '国内',
    1: '国际',
    2: '军事',
    3: '体育',
    4: '社会',
    5: '娱乐',
    6: '财经'
}

if __name__ == '__main__':
    print(get_stop_words_list())
