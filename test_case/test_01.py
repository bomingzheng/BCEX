# 数据库数据进行比对
from test_tools.reflect import Method
from test_tools.do_mysql import SshMySQl
import unittest
from api_public.requests_method import Requests
import json
from test_tools.read_excel import DoExcel
from ddt import ddt, data
from test_tools.read_logs import MyLog   # 到日志的类包
from test_tools.gain_path import *  # 到路径的类的包
my_log = MyLog()  # 调用实例
date = DoExcel.get_excel(test_excel_path)   # 调用读取excel数据的方


@ddt
class TestCase(unittest.TestCase):
    @data(*date)
    def test_01(self, i):
        if i['data'].find("${order_nos}") != -1:   # 在data找到这个标签就替换
            if getattr(Method, 'order_nos') == None:  # 判断反射属性是空值，如果为空查询数据库并赋值
                que_sql = "SELECT order_no FROM `order` WHERE user_id=6865 ORDER BY id DESC LIMIT 1"
                order_nos = SshMySQl().do_mysql(que_sql)[0][0]
                i['data'] = i['data'].replace("${order_nos}", str(order_nos))  # 把变量标签替换
                setattr(Method, 'order_nos', order_nos)  # 把新值存到反射里面
            else:   # 如果不是直接通过反射获取
                i['data'] = i['data'].replace("${order_nos}", str(getattr(Method, 'order_nos')))
        if i['check_sql']!= None:  # 判断excel表这个标题下有语句时
            # 拿到excel里面sql语句，存在字典通过键取值，需要eval
            que_sql = eval(i['check_sql'])['sql']
            # 调用查询连接数据库的类，开始查询
            before_amount = SshMySQl().do_mysql(que_sql)[0][0]
            my_log.info('用例{}的查询下单之前的锁定资产{}'.format(i['case_id'], before_amount))
            # 进行接口请求
            r = Requests().public(i['url'], eval(i['data']), eval(i['headers']), i['method'])
            # 请求之后锁定资产
            after_amount = SshMySQl().do_mysql(que_sql)[0][0]
            my_log.info('用例{}的查询下单之后的锁定资产{}'.format(i['case_id'], after_amount))
            # # 检查锁定资产是否正确
            if (int(eval(after_amount)))-(int(eval(before_amount))) == int(eval(i['date'])['amount']):
                my_log.info('数据库校验通过')
                check_res = '锁定金额正确'
            else:
                my_log.info('数据库校验失败')
                check_res = '锁定金额不正确'
                # 不管金额正确与否，都把结果写回excel
            DoExcel.write_back(test_excel_path, i['sheet_name'], i['case_id']+1, 10, check_res)

        else:  # 如果不用检查sql语句直接发送请求
            r = Requests().public(i['url'], eval(i['data']), eval(i['headers']), i['method'])
        try:
            # 要判断对比的类型要一致
            self.assertEqual(i['expected_result'], r.json()['code'])
            test = 'PASS'  # 用例执行通过
        except AssertionError as e:
            test = 'Failed'  # 用例执行失败
            my_log.error('执行用例出错了！{}'.format(e))
            raise e
            # excel只能写入int和str需要转换
        finally:  # 无论报不报错，里面的代码都要执行
            # 调用写入的方法，以case_id为行号因为有标题所以case_id+1，传入测试结果写回到excel
            DoExcel.write_back(test_excel_path, i['sheet_name'], i['case_id'] + 1, 10, str(r.json()))
            # 把对比结果写回到excel
            DoExcel.write_back(test_excel_path, i['sheet_name'], i['case_id'] + 1, 11, str(test))
            # 测试结果写到日志
            my_log.info('获取的测试用例是：{0},测试结果是：{1}'.format(i['case_id'], r.json()))


if __name__ == '__main__':
    unittest.main()


