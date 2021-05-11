import xlrd
from xlutils.copy import copy
import pandas as pd
import collections
# 打开文件
workbook = xlrd.open_workbook('模型和算子列表v2.0.xlsx')


# 查看工作表
print("sheets：" + str(workbook.sheet_names()))
table = workbook.sheet_by_name('Sheet1')
myDict = collections.defaultdict(int)
l = len(table.col_values(0))
print(l, table.col)
for i in range(10):
    for j in range(1, len(table.col_values(i))): 
        # print(i, j)
        myDict[table.col_values(i)[j]] += 1
for k, v in sorted(myDict.items(), key = lambda kv:(-kv[1], kv[0])):
    print("{} {}".format(k, v))
# for k, v in myDict.items():
#     print("{} {}".format(k, v))