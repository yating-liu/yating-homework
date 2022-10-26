import os
import shutil


def get_file_list(old_path):
    file_list =[]
    for path, dirs, files in os.walk(old_path):
        for file in files:
            file_list.append(os.path.join(path,file))
            # print(file_list)
    return file_list

# get_file_list(old_path)

def parse_filename(old_path):
    filepath, suffix = os.path.splitext(old_path)
    name, light, position, label = filepath.split('/')[-4:]
    label = label.split('_')[-1]
    return name, light, position, label

#parse_filename(old_path)

def makedirs(filepath):
    if not os.path.exists(filepath):
        os.makedirs(filepath)

def mycopyfile(srcfile,dstfile):
    if not os.path.isfile(srcfile):
        print("%s not exist!"%(srcfile))
    else:
        fpath,fname=os.path.split(dstfile)
        if not os.path.exists(fpath):
            os.makedirs(fpath)
        shutil.copyfile(srcfile,dstfile)
        print("copy %s -> %s"%( srcfile,dstfile))

def main():
    old_path = './20211223'
    light = ['l01','l02','l04']
    label_type = ['attentive']

    new_path = f'{old_path}_result'
    mymakedirs(dst_path)

    file_list =get_file_list(old_path)

    for file1 in file_list:
        name, light_level, position, label = parse_filename(file1)
        if light in light_level and label in label_type:
            file1_path, file1_name = os.path.split(file1)
            new_path = f"{new_path}/{name}/{position}/{light}/{file1_name}"
            mycopyfile(file1, new_path)


if __name__ == '__main__':
    main()
