# 返回的JSON结果封装类
import json


# 基本的result类
class Result:
    # 成功
    SUCCESS = 0
    # 失败
    FAIL = 1

    def __init__(self, items=None, code=SUCCESS, msg='success'):
        if items:
            self.data = {}
            self.data['items'] = items
        self.code = code
        self.msg = msg

    def to_json(self):
        return json.dumps(self.__dict__)


# 带分页的result类
class PageResult(Result):
    def __init__(self, items=None, count=0, code=Result.SUCCESS, msg='success'):
        if items:
            self.data = {}
            self.data['items'] = items
            self.data['count'] = count
        self.code = code
        self.msg = msg


if __name__ == '__main__':
    items = None
    result = Result(items=items)
    print(result.to_json())
    print(type(result.__dict__))
    print(type(json.dumps(result.__dict__)))
    result = Result(code=Result.FAIL, msg='')
    print(result.to_json())

