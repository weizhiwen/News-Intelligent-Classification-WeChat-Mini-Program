from datetime import datetime, date, timedelta


# 格式化日期函数，start_date 为开始日期（默认为当前日期），days 为倒推的天数
def get_format_news_date(date=date.today(), days=0):
    start_date = datetime(date.year, date.month, date.day)
    # 返回格式化好的字符串
    return (start_date).strftime("%Y/%m%d")


if __name__ == '__main__':
    special_date = date.today()
    print(special_date)
    print(get_format_news_date(special_date))
    print('http://www.chinanews.com/scroll-news/{}/news.shtml'.format(get_format_news_date(special_date)))
    next_date = special_date + timedelta(days=-1)
    print(next_date)
    print(get_format_news_date(next_date))
    print('http://www.chinanews.com/scroll-news/{}/news.shtml'.format(get_format_news_date(next_date)))
