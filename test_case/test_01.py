__author__ = 'Bomz'
import unittest
from api_public.requests_method import Requests
import json
from test_tools.read_excel import DoExcel
from ddt import ddt, data
from test_tools.gain_path import *
from test_tools.read_logs import MyLog   # 到日志的类包
from test_tools.gain_path import *  # 到路径的类的包
my_log = MyLog()  # 调用实例

date = DoExcel.get_excel(test_excel_path)   # 调用读取excel数据的方法


@ddt
class Test(unittest.TestCase):

    @data(*date)
    def test_01(self, i):
        try:
            r = Requests().public(i['url'], eval(i['data']), eval(i['headers']), i['method'])
            # 要判断对比的类型要一致
            self.assertEqual(i['expected_result'], r.json()['code'])
            TestResult = 'PASS'   # 用例执行通过
        except AssertionError as e:
            TestResult = 'Failed'   # 用例执行失败
            my_log.error('执行用例出错了！{}'.format(e))
            raise e
            # excel只能写int和str需要转换
        finally:  # 无论报不报错，里面的代码都要执行
            # 把测试结果写会到excel，调用写入的方法，以case_id为行号，传入测试结果和比对结果，因为有标题所以case_id+1
            DoExcel.write_back(test_excel_path, i['sheet_name'], i['case_id']+1, str(r.json()), TestResult)
            my_log.info('获取的测试结果是：{}'.format(r.json()))


if __name__ == '__main__':
    unittest.main()
