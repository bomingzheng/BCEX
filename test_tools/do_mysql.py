__author__ = 'Bomz'
import pymysql
from sshtunnel import SSHTunnelForwarder



class SshMySQl(object):

    def do_mysql(self, sql, select='all'):
        with SSHTunnelForwarder(('52.79.247.255', int(22)),
                                ssh_pkey='C:\\Users\\bomin\\Desktop\\data\\数据库\\id_rsa_2048',
                                ssh_password="Uxin9527&",
                                ssh_username='bcex_mysql',
                                remote_bind_address=('bcex-release.cnhbjn4dkymy.ap-northeast-2.rds.amazonaws.com',
                                                     int(3306))) as server:
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
    connect = SshMySQl().do_mysql('SELECT order_no FROM `order` WHERE user_id=6865 ORDER BY id DESC LIMIT 1')
    print(int(connect[0][0]))
