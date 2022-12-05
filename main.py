import os
import re
from PIL import Image
import sys


name = 'main'


def get_picture(img_path,img_type_to_get):
    img = img_path+'\\'+img_type_to_get
    files = []
    for path in os.listdir(img_path):
        # check if we are in folder or if it is a file
        if os.path.isfile(os.path.join(img_path,path)):
            files.append(path) # get every files in the folder, ignore all other folder
    return creat_new_img(open_all_file(separate_files_by_typed(files,img_type_to_get,img_path),img_path),img_path)


def separate_files_by_typed(files, type, path):
    file_typed = []
    # remove any file we wouldn't want (wrong type)
    for e in files :
        k=0
        for i in range(len(e)):
            if e[i].upper() == type[k].upper():
                k = k+1
            if k == len(type):
               file_typed.append(e)
        file_to_oppen = []
    for e in file_typed:
        file_to_oppen.append(path+'\\'+e)
    creat_new_img(file_to_oppen,path)
    return file_typed


def open_all_file(files_to_oppen,files_path):
    file_open = []
    for e in files_to_oppen:
        path = files_path + "\\" + e
        file_open.append(open(path))
    return file_open


def creat_new_img(file_open,path):
    # oppen all the image
    img = []
    for e in file_open:
        print(e)
        f = Image.open(e)
        img.append(f)
    # find the size of all image
    img_size = []
    for e in img:
       img_size.append(e.size)
    # creat a new image with the correct size
    length = 0
    for e in img_size:
        length = length + e[1]
    new_img = Image.new('RGB', (img_size[0][0], length),(250,250,250))
    emplacement_x= 0
    emplacement_y= 0
    # place the file where they should be to be past
    for e in range(len(img)):
        new_img.paste(img[e],(emplacement_y, emplacement_x))
        emplacement_x = emplacement_x + img_size[e][1]

    # creat path for final folder

    creat_new_path = True
    for e in os.listdir(path):
        if e == 'Final_image':
            print(f'Path {path} all ready exist no new path created')
            creat_new_path = False
    path = path + '\\Final_image'
    if creat_new_path :
        os.mkdir(path)
    # save the PDF
    path_and_name_pdf = path+'\\final.PDF'
    new_img.save(path_and_name_pdf)


def chelp():
    pass


def main(argv):
    img_type = "PNG"
    flag = {'-h': [chelp, None, None],
            '-i': [get_picture, r'.:\.*', img_type]}
    for i in range(len(argv)):
        arg = argv[i]
        if flag.keys().__contains__(arg):
            if flag[arg][1] is None or re.search(flag[arg][1], argv[i+1]):
                flag[arg][0](argv[i+1], flag[arg][2])


if name == 'main':
    main(sys.argv[1:])
