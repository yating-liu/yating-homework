import os
import shutil
import numpy as np
import pandas as pd
import csv

filepath = '/home/liuyating/Downloads/homework/20211228'

def get_file_list(filepath, types=['.csv'], is_sort = True):
    file_list = []
    for path, dirs, files in os.walk(filepath):
        for file in files:
            if os.path.splitext(file)[1] in types:
                file_list.append(os.path.join(path, file))
    if is_sort:
        file_list.sort()
        # print(file_list)
    return file_list

# get_file_list(filepath, types=['.csv'])

def parse_filename(filepath):
    filepath, suffix = os.path.splitext(filepath)
    name, light_level, position, label = filepath.split('/')[-4:]
    label = label.split('_')[-1]
    return name, light_level, position, label




def calculate(data):
    starTime = int(data[0])
    endTime = int(data[1])



# data1 = list(csv.reader(open('inattentive.csv')))
# print(data1.ix[[0,1,3],:])

# for i, row in enumerate(data[1:],1):
#     data[i] = [int(elt) if elt.isdigit() else elt for elt in row]
#     points = {} # an empty dictionary
# for i, country in enumerate(data[0][2:],2):

#新建文件
# open("test.csv",'w').close()
# #写入内容
# with open("./test.csv", 'a') as cf:
#     write = csv.writer(cf)
#     write.writerow(['名字', '0', '2', '3', '4', '5'])
#     data =  [str(person), str(0_time), str(2_time), str(3_time), str(4_time), str(4_time)]
#     for i in data:
#         write.writerow(i)



if __name__ == '__main__':
    main()
