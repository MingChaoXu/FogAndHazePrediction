# coding=utf-8
"""
@author: 许铭潮
"""
import xlrd
import csv
import pandas as pd

def write_csv(results, file_name):
    with open(file_name, 'r') as f:
        writer = csv.writer(f)
        # writer.writerow(['id', 'label'])
        writer.writerows(results)


data = xlrd.open_workbook('../data/data.xlsx')
table = data.sheets()[0]
nrows = table.nrows  # 行数
ncols = table.ncols  # 列数
train_data_nums = int(nrows*0.75)
test_data_nums = nrows-train_data_nums

# 训练集
with open('../data/train.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for i in range(0, train_data_nums):
        rowValues = table.row_values(i)  # 某一行数据
        rowValues[0] = i-1
        if i == 0:
            # print(rowValues[:-1])
            rowValues[0] = 'id'
            writer.writerow(rowValues[:-1])
        else:
            writer.writerow(rowValues[:-1])
        # print(rowValues[:-1])

# 测试集
with open('../data/test.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for i in range(0, test_data_nums):
        rowValues = table.row_values(i+train_data_nums)  # 某一行数据
        rowValues[0] = i-1
        if i == 0:
            rowValues = table.row_values(i)
            # print(rowValues[:-1])
            rowValues[0] = 'id'
            writer.writerow(rowValues[:-1])
        else:
            writer.writerow(rowValues[:-1])
        # print(rowValues[:-1])

