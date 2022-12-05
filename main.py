import os
import re
from PIL import Image
import sys

def get_picture(img_path):
    files = []
    regex = r'\.png$'
    for path in os.listdir(img_path):
        # check if we are in folder or if it is a file
        if os.path.isfile(os.path.join(img_path,path)):
            files.append(path) # get every file in the folder, ignore all others folder
    lst_img = [img_path+'\\'+e for e in files if re.search(regex,e.lower())]
    return creat_new_img(lst_img, img_path)



def open_all_file(files_to_oppen,files_path):
    file_open = []
    for e in files_to_oppen:
        path = files_path + "\\" + e
        file_open.append(open(path))
    return file_open


def creat_new_img(file_open,path):
    # oppen all the image

    # creat a new image with the correct size
    length = 0
    img = []
    img_size = []
    for e in file_open:
        print(e)
        f = Image.open(e)
        img.append(f)
        img_size.append(f.size)
        length = length + f.size[1]
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
    flag = {'-h': [chelp, None],
            '-i': [get_picture, r'.:\.*']}
    for i in range(len(argv)):
        arg = argv[i]
        if flag.keys().__contains__(arg):
            if flag[arg][1] is None or re.search(flag[arg][1], argv[i+1]):
                flag[arg][0](argv[i+1])


if __name__ == '__main__':
    main(sys.argv[1:])
