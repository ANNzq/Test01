# from pyspark import SparkConf, SparkContext
# conf = SparkConf().setMaster("local[*]").setAppName("text_spark_app")
# sc = SparkContext(conf=conf)
# # rdd1 = sc.textFile("")
# # print(sc.version)
# rdd1 = sc.textFile("E:/0519MAP/123.txt")
# print(rdd1.collect())
# sc.stop()
#
# # 创建excel
# import xlwt                          # 0.导入xlst模块
#
# wb = xlwt.Workbook()                 # 1.创建 Workbook
# count=3
# ws = wb.add_sheet('test_sheet')      # 2.创建 worksheet
# list = [0,9,6,4]
# # 3.写入第一行内容  ws.write(a, b, c)  a：行，b：列，c：内容
# ws.write(0, 0, list[1])
# ws.write(0, 1, '号码')
# ws.write(0, 2, '姓名')
# ws.write(0, count, list[2])
#
# # 保存文件
# wb.save('E:/myExcel.xls')
# from tkinter import Label, Tk, Entry

# import os
# from pyspark import SparkConf, SparkContext
# os.environ['PYSPARK_PYTHON'] = 'C:/Users/zhangqian/PycharmProjects/pythonProject/venv/Scripts/python.exe'
# os.environ['HADOOP_HOME'] = "D:/hadoop-3.0.0/hadoop-3.0.0"
# conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
# conf.set("spark.default.parallelism","1")
# sc = SparkContext(conf=conf)
# rdd1 = sc.parallelize([1,2,3,4,5])
# rdd2 = sc.parallelize([("hello",3),("spark",5),("hi",7)])
# rdd3 = sc.parallelize([[1,3,5],[6,7,9],[11,13,11]])
# rdd1.saveAsTextFile("D:/output1")
# rdd2.saveAsTextFile("D:/output2")
# rdd3.saveAsTextFile("D:/output3")


# # 首先导入tk
# import tkinter as tk
#
# #定义窗口
# window = tk.Tk()
# window.title('请输入要查找的名称')
# window.geometry('200x140')
# #定义一个输入文本框
# entry = tk.Entry(window, show="*")
# #表示输入的字符以*号的形式出现
# entry = tk.Entry(window, show=None)
# #对文本框内容进行打包
# entry.pack()
# #将输入的字符赋值给var
# var = entry.get()
# print(var)
# window.mainloop()

# -*- coding:utf8 -*-
# import xlrd
# import os
#
# from xlrd.timemachine import xrange
#
# id = u'85028'
#
# def find(path,id):
#     for rt, dirs, files in os.walk(path):
#         for f in files:
#             if f != ".DS_Store":
#                 path = rt+os.path.sep+f
#                 workbook = xlrd.open_workbook(path)
#                 sheet_names = workbook.sheet_names()
#                 all_value = workbook.sheet_by_index(0)
#                 length = all_value.nrows
#                 for i in xrange(length):
#                     row = all_value.row_values(i)
#                     if id in row[0]:
#                         print(row[1].encode('utf8'),row[8])
#                     # print path
#                     # break
# def raw_input(param):
#     pass
#
# if __name__ == "__main__":
#     path = r"/Users/liruopeng/Downloads/score/english"
#     while 1:
#         nID = raw_input("请输入名字：")
#         find(path,nID)

import tkinter as tk
from tkinter import filedialog
# 获取选择文件路径
# 实例化
root = tk.Tk()
root.withdraw()
# 获取文件夹路径
f_path = filedialog.askopenfilename()
print('\n获取的文件地址：', f_path)
