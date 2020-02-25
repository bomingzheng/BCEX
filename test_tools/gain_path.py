__author__ = 'Bomz'
import os

# 设置文件路径的可配置
# os.path.realpath(__file__)  # 查看当前文件绝对路径
project_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
# 测试数据路径（excel）
test_excel_path = os.path.join(project_path, 'test_data', 'information', 'test.xlsx')
# 测试报告路径
test_report_path = os.path.join(project_path, 'test_result', 'report', 'api.html')
# 测试用例路径
test_case_path = os.path.join(project_path, 'test_case')
# 配置文件的路径
test_config_file = os.path.join(project_path, 'test_data', 'conf', 'config_file.config')
# 配置日志文件路径
test_log_path = os.path.join(project_path, 'test_result', 'test_logs', 'bcex_log.txt')


if __name__ == '__main__':

    print(project_path)
    print(test_excel_path)
    print(test_report_path)
    print(test_config_file)
