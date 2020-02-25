__author__ = 'Bomz'

from api_public.requests_method import Requests
from test_tools.read_excel import DoExcel
import json
import time
import test_data.HTMLTestRunnerNew as HTMLTestRunner
import unittest

from test_tools.gain_path import *
from steadily.requests_9 import TestCase

# 创建测试套件实例
suite = unittest.TestSuite()
# 单条用例
# suite.addTest(Test('test_01'))  # 导入包通过添加case添加测试类，添加测试用例运行测试。
# 逐条添加想执行的case，顺序也是从上而下
# suite.addTest(Test('test_two_negative'))
'''
for i in test_data:
     suite.addTest(Test('test_01', i['url'], eval(i['data']), i['method'], eval(i['headers'])))
如果是参数化没通过初始化函数传参时，用循环添加参数的方式执行。test_01执行的用例名称，后面是需要的参数
'''
# 多条用例
load = unittest.TestLoader()  # 创建加载用力的容器
# 执行测试类下的所有用例
suite.addTest(load.loadTestsFromTestCase(TestCase))
# 执行模块下所有的类,首先  从路径目录导入模块名，不是导入模块的类
# suite.addTest(load.loadTestsFromModule('模块名称'))
# 执行目录下所有的模块
# suite = unittest.defaultTestLoader.discover(r"D:\koko\APX\test_case", pattern="test*.py")   # 目录路径，文件以定义开头的
# 指定存放报告的路径

# 报告存放
# 报告存放路径，且根据当前时间命名

# file_path = r"D:\koko\APX\test_result\report\{}.html".format(time.strftime("%Y_%m_%d %H_%M_%S"))  # 以绝对路径
# 运行测试套件
with open(test_report_path, 'wb')as f:
    # 实例化TextTestRunner类,stream 数据流=数据写在哪,verbosity=2信息最详细,title=标题, description=描述
    # 运行run方法（）把suite放到run里面
    HTMLTestRunner.HTMLTestRunner(stream=f, title='报告', description='下单接口报告', tester='Bomz').run(suite)


