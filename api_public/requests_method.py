__author__ = 'Bomz'
import requests
from test_tools.read_logs import MyLog   # 到日志的类包
from test_tools.gain_path import *  # 到路径的类的包
my_log = MyLog()  # 调用实例


class Requests(object):

    def public(self, url, data, headers, method):

        try:
            if method.upper() == 'GET':
                return requests.get(url, json=data, headers=headers)
            elif method.upper() == 'POST':
                return requests.post(url, json=data, headers=headers)
            else:
                my_log.error('输入请求方法错误！')
        except Exception as e:
            my_log.error('出错了！{}'.format(e))
            raise e


if __name__ == '__main__':
    Requests().public()