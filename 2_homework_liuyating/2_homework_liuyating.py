import os
import shutil
import numpy as np
import pandas as pd
import csv



def get_file_list(filepath, types=[], is_sort = True):
    file_list = []
    for path, dirs, files in os.walk(filepath):
        for file in files:
            if os.path.splitext(file)[1] in types:
                file_list.append(os.path.join(path, file))
    if is_sort:
        file_list.sort()
        # print(file_list)
    return file_list



def parse_filename(filepath):
    filepath, suffix = os.path.splitext(filepath)
    name, light_level, position, label = filepath.split('/')[-4:]
    label = label.split('_')[-1]
    return name, light_level, position, label

def filter_file_list(file_list, lights = [], positions=[], names=[], labels=[]):
    return list(filter(lambda x: filter_by_attributes(x, lights, positions, names, labels), file_list))

def filter_by_attributes(filepath, lights = ['l01'], positions=[], names=[], labels=[]):
    name, light_level, position, label = parse_filename(filepath)
    if lights:
        if light_level not in lights:
            return False
    if positions:
        if position not in positions:
            return False
    if names:
        if name not in names:
            return False
    if labels:
        if label not in labels:
            return False
    return True

def makedirs(filepath):
    if not os.path.exists(filepath):
        os.makedirs(filepath)

def read_csv(filepath):
    with open(filepath) as df:
        myread = csv.reader(df)
        mylist = myread.tolist()
        return mylist


def write_csvdata(filepath, myList):
        with open(filepath) as cf:
            mywrite = csv.writer(cf)
            mywrite.writerow(myList)


def compute_csv_time(data):
    rows = read_csv(filepath)
    for row in rows:
        row[1] - row[0]
        classifacation


def main():
    filepath = '/home/liuyating/Downloads/homework/20211228'
    file_list = get_file_list(filepath, types = ['.csv'], is_sort = True)
    file_list = filter_file_list(file_list, lights = ['mylight'], positions=['myposition'], names=[], labels=['mylabel'])
    mylight = ['l01']
    myposition = ['p04']
    mylabel = ['attentive', 'inattentive']


    for attentive_file in file_list:
        name, light_level, position, label = parse_filename(filepath)
        class0, class2, class3, class4, class5 = 0 , 0 , 0 , 0 , 0
        inattentive_file = filepath.replace('attentive', 'inattentive')
        class0 = compute_csv_time(attentive_file)
        class2, class3, class4, class5 = compute_csv_time(inattentive_file)
        row = ','.join(name,class0,class2, class3, class4, class5 )
        write_csvdata(result_file, row)



if __name__ == '__main__':
    main()



