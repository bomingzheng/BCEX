# 正则表达式
import re
from test_tools.reflect import Method
# s = 'www.baidu.com'
# res = re.match('(w)(ww)', s)  # 从s匹配www，头匹配从头匹配不符合就报错
# print(res.group(2))  # group根据括号分组，group默认就是0展示www数据，1展示w，2展示ww

# s = 'hellogoodmonkey'
# res = re.findall('good', s)   # 匹配所有，不只是头，返回一个列表 匹配的内容存在列表，不支持group
# res = re.findall('(he)(llo)', s)  # 支持分组，分成一个列表嵌套元祖[('he','llo')]
# print(res)
class DoRegx:
    @staticmethod
    def do_re(s):  # 传入数据
        while re.search('\${(.*?)}', s):   # 从数据匹配${XX} 这种格式的数据并分组，0整个数据，1就是没有括号的xxx
            key = re.search('\${(.*?)}', s) .group(0)  # 从s取出${amount},search需要跟group组合运行
            value = re.search('\${(.*?)}', s) .group(1)   # value直接去掉括号的数据
            s_1 = s.replace(key, str(getattr(Method, value)))  # 传入变量，该变量和反射属性名称对等
            return s_1


if __name__ == '__main__':
    s = s_1 = ' {"order_nos":json.dumps(["${order_nos}"]), "api_key": "c8863ec11ee3d908ae40fc98a98f4804", "sign": "qa"}'
    print(DoRegx.do_re(s))

