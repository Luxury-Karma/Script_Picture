import os
from PIL import Image



def get_picture():
    img_path = 'C:\\Users\\PC\\Pictures\\server screen shot\\4'
    img_type_to_get = '.png'
    img = img_path+'\\'+img_type_to_get
    files = []
    for path in os.listdir(img_path):
        #check if we are in folder or if it is a file
        if os.path.isfile(os.path.join(img_path,path)):
            files.append(path) #get every files in the folder, ignore all other folder
    creat_new_img(open_all_file(Separate_files_by_typed(files,img_type_to_get,img_path),img_path))
#    print(f'absolute Path : {img} ,\nimage name : {img_type_to_get},\n folder path : {img_path}')
#    img_file = open(img,'r')
#    print(f'file: {img_type_to_get} is Open')


def Separate_files_by_typed(files, type,path):
    file_typed = []
    #remove any file we wouldn't want (wrong type)
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
    creat_new_img(file_to_oppen)
    return file_typed


def open_all_file(files_to_oppen,files_path):
    file_Oppen = []
    for e in files_to_oppen:
        path = files_path + "\\" + e
        file_Oppen.append(open(path))
    return file_Oppen

def creat_new_img(file_oppen):
    for e in file_oppen:
        img = Image.open(e)
        r,g,b=img.split()
        img = Image.merge("RGB",(b,g,r))
        img.show()

get_picture()