__author__ = 'Bomz'

import unittest
from api_public.requests_method import Requests
import json
from test_tools.read_excel import DoExcel
from ddt import ddt, data
from test_tools.gain_path import *


date = DoExcel(test_case_path, 'remove').get_excel()   # 调用读取excel数据的方法


@ddt
class Test(unittest.TestCase):

    @data(*date)
    def test_01(self, i):
        r = Requests().public(i['url'], eval(i['data']), eval(i['headers']), i['method'])

        try:
            # 要判断对比的类型要一致
            self.assertEqual(i['expected_result'], r.json()['code'])
            TestResult = 'PASS'   # 用例执行通过
        except AssertionError as e:
            TestResult = 'Failed'   # 用例执行失败
            print('执行用例出错了！'.format(e))
            raise e
            # excel只能写int和str需要转换
        finally:  # 无论报不报错，里面的代码都要执行
            # 把测试结果写会到excel，调用写入的方法，以case_id为行号，传入测试结果和比对结果，因为有标题所以case_id+1
            DoExcel(test_case_path, 'remove').write_back(i['case_id']+1, str(r.json()), TestResult)
            print('获取的测试结果是：{}'.format(r.json()))


if __name__ == '__main__':
    unittest.main()
