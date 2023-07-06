import codecs
import re
import numpy as np
import xlwt

f = codecs.open('E:/MAP_Analyze_1.txt', mode='r', encoding='utf-8')  # 打开txt文件，以‘utf-8'编码读取
line = f.readline()  # 以行的形式进行读取文件
x = []  # 设置x y z数组
y = []
z = []
while line:
    a = re.split(r"\s+",line) # 每行数据分隔情况，此数据以“ ”分隔
    # 选取需要读取的数据列数
    # print(a)
    b0 = a[0] # 起始地址
    b1 = a[1] # 结束地址
    b2 = a[2] # 内存大小
    b3 = a[3] # 变量类型
    b4 = a[4] # 名字
    # print(type(a))
    # print(type(a[0]))
    # print(line)
    # print(line[0])
    # print(type(line))
    # print(b2)
    # print(a[4])
    x.append(b4)  # 将其添加在列表之中
    y.append(b2)

    line = f.readline()
f.close()  # close文件
ff = open(r'E:/new1.xls', 'a')  # 对获取的txt前两列数据进行保存

for i in x:
    print(i, file=ff)
for j in y:
    print(j, file=ff)

ff.close()