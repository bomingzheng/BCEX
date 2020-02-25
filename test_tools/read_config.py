__author__ = 'Bomz'
import configparser  # 导入配置文件包
from test_tools.gain_path import *


class ReadConfig:
    @staticmethod  # 用静态方法，不用实例化
    def get_config(file_path, section, option):  # 传入配置文件, 区域值，选项值
        cf = configparser.ConfigParser()
        cf.read(file_path)
        return cf[section][option]


if __name__ == '__main__':

    print(ReadConfig.get_config(test_config_file, "DB", "db_data"))