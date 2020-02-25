import pandas as pd
df = pd.read_excel(r'D:\koko\APX\test_data\information\test.xlsx')# 默认读第一个表单
# print(df.values)        # 全部数据嵌套的列表
# .ix已被弃用
# loc——通过行标签索引行数据,iloc——通过行号索引行数据
# print(df.iloc[0, 0])  # 通过行号索引读取数据,从0开始标题栏不算
# print(df.iloc[:]) # 展示所有的数据索引
# print(df.iloc[:].values)  # 呈矩阵样式展示全部数据
# print(df.loc[:, ['data']].values)  # 通过标签索引读取data标题下所有的数据，列表嵌套
# print(df.loc[:, ['data']])   # 通过标签索引读取data标题下所有的数据，数据展示不全用...表示
# print(df.loc[:, ['data','url'], ].values)  # # 通过标签索引读取多标签的数据
# 打印指定行和列的数据变转成字典形式
# print(df.loc[1, ['case_id','url', 'data', 'headers', 'method'], ].to_dict())
# print(df.index.values)  # 打印excel的数据索引值
test_data = []
for i in df.index.values:
    row_data = df.loc[i, ['case_id', 'title', 'url', 'data', 'headers', 'method', 'expected_result'], ].to_dict()
    test_data.append(row_data)

print(test_data)