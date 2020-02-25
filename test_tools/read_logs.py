import logging
from test_tools.gain_path import *


class MyLog:

    def my_log(self, msg, level):
        my_logger = logging.getLogger(test_log_path)    # 定义一个日志收集器
        my_logger.setLevel('INFO')                    # 设置日志级别
        # 设置日志输出格式
        formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s')
        ch = logging.FileHandler(test_log_path, encoding='utf-8')  # 以该格式输出到文件名称和文字格式
        # # 设置日志输出级别
        ch.setLevel('INFO')
        ch.setFormatter(formatter)   # 以指定格式指定级别输出
        my_logger.addHandler(ch)        # 互通收集和输出渠道
        if level == 'DEBUG':        # 判断传入的lever信息输出响应的信息
            my_logger.debug(msg)
        if level == 'INFO':
            my_logger.info(msg)
        if level == 'ERROR':
            my_logger.error(msg)
        if level == 'WARNING':
            my_logger.warning(msg)
        if level == 'CRITICAL':
            my_logger.critical(msg)

        my_logger.removeHandler(ch)  # 关闭渠道，每次输出重新开启否则会重复打印

    def debug(self, msg):
        self.my_log(msg, 'DEBUG')

    def info(self, msg):
        self.my_log(msg, 'INFO')

    def error(self, msg):
        self.my_log(msg, 'ERROR')

    def warning(self, msg):
        self.my_log(msg, 'WARNING')

    def critical(self, msg):
        self.my_log(msg, 'CRITICAL')


if __name__ == '__main__':
    m = MyLog()
    m.my_log('你是最棒的', 'INFO')










