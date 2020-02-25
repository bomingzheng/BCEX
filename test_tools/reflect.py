import pandas as pd
from test_tools.gain_path import *
from test_tools.read_config import ReadConfig


class Method:
    amount = pd.read_excel(test_excel_path, sheet_name='init') .iloc[0, 0]
    order_nos = None


if __name__ == '__main__':
    print(Method.order_nos)