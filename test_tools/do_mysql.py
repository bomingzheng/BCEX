__author__ = 'Bomz'
import pymysql
from sshtunnel import SSHTunnelForwarder
from test_tools.gain_path import *
from test_tools.read_config import ReadConfig


class SshMySQl(object):

    def do_mysql(self, sql, select='all'):
        with SSHTunnelForwarder(('52.79.247.255', int(22)),
                                ssh_pkey=r'C:\Users\bomin\Desktop\data\工作数据\api\bcex_data_ssh',
                                ssh_username='bcex_mysql',
                                remote_bind_address=('bcex-release.cnhbjn4dkymy.ap-northeast-2.rds.amazonaws.com', int(3306))) as server:
            conn = pymysql.connect(host='127.0.0.1',
                                   port=server.local_bind_port,
                                   user='bomingzheng',
                                   password='U2l0pVZUHZsC5x7C',
                                   database='bcex_release',
                                   charset='utf8')
            cursor = conn.cursor()
            try:
                cursor.execute(sql)
                if select == 'all':
                    result = cursor.fetchall()   # 返回的是列表嵌套元祖，多条数据
                else:
                    result = cursor.fetchone()   # 单条数据，返回的是元组
            except Exception as e:
                print('Error：执行操作失败{}'.format(e))
            cursor.close()
            conn.close()
            server.close()
            return result


if __name__ == "__main__":
    connect = SshMySQl().do_mysql('select balance from asset_user_sum_locked WHERE account_id=2910995')
    print(int(connect[0][0]))
