from pymongo import MongoClient


# MongoDB 封装类
class MongoDB:
    # 构造方法
    def __init__(self, db, collection, host='localhost', port=27017, username=None, password=None):
        self.host = host
        self.port = port
        self.client = MongoClient(host=host, port=port, username=username, password=password)
        self.db = self.client[db]
        self.collection = self.db[collection]
