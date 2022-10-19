import os
import shutil


filepath ='./20211223'

persons = ['keweijie','liuyang','liyalun']
lights = ['l01','l02','l03','l04']
positions = ['p01','p02','p04']


for person in persons:
    for light in lights:
        for position in positions:
            if not os.path.exists(f'./20211223_2/{person}/{position}/{light}'):
                os.makedirs(f'./20211223_2/{person}/{position}/{light}')

def get_file_list(filepath):
    file_list =[]
    for path, dirs, files in os.walk(filepath):
        for file in files:
            file_list.append(os.path.join(path,file))
            # print(file_list)
    return file_list

# get_file_list(filepath)

def parse_filename(filepath):
    for file in get_file_list(filepath):
        person = file.split('/')[-4]
        light = file.split('/')[-3]
        position = file.split('/')[-2]
        label = file.split('/')[-1]
        path = f'./20211223_2/{person}/{position}/{light}/{label}'
        # print(person,position,light,label)
        if light != 'l03':
            if label == 'attentive.bin':
                # print(file)
                shutil.copyfile(file, path)


parse_filename(filepath)


