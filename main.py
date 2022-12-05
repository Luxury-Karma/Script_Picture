import os
from PIL import Image
import sys
import aspose.words as aw


def get_picture(img_path,img_type_to_get):
    img = img_path+'\\'+img_type_to_get
    files = []
    for path in os.listdir(img_path):
        #check if we are in folder or if it is a file
        if os.path.isfile(os.path.join(img_path,path)):
            files.append(path) #get every files in the folder, ignore all other folder
    return creat_new_img(open_all_file(Separate_files_by_typed(files,img_type_to_get,img_path),img_path),img_path)
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
    creat_new_img(file_to_oppen,path)
    return file_typed


def open_all_file(files_to_oppen,files_path):
    file_Oppen = []
    for e in files_to_oppen:
        path = files_path + "\\" + e
        file_Oppen.append(open(path))
    return file_Oppen

def creat_new_img(file_oppen,path):
    #oppen all the image
    img = []
    for e in file_oppen:
        print(e)
        f = Image.open(e)
        img.append(f)
    #find the size of all image
    img_size = []
    for e in img:
       img_size.append(e.size)
    #creat a new image with the correct size
    length = 0
    for e in img_size:
        length = length + e[1]
    new_img = Image.new('RGB', (img_size[0][0], length),(250,250,250))
    emplacementX= 0
    emplacementY= 0
    #place the file where they should be to be past
    for e in range(len(img)):
        new_img.paste(img[e],(emplacementY,emplacementX))
        emplacementX = emplacementX + img_size[e][1]


    #creat path for final folder

    creat_new_path = True
    for e in os.listdir(path):
        if e == 'Final_image':
            print(f'Path {path} all ready exist no new path created')
            creat_new_path = False
    path = path + '\\Final_image'
    if creat_new_path :
        os.mkdir(path)
    #save the image
    path_and_name_PNG = path+'\\final.PNG'
    new_img.save(path_and_name_PNG, 'PNG')
    path_and_name_PDF = path+'\\final.PDF'
    #new_img.show()
    #change PNG to PDF
    doc = aw.Document()
    builder = aw.DocumentBuilder(doc)
    builder.insert_image(path_and_name_PNG)
    doc.save(path_and_name_PDF)
    os.remove("path_and_name")


    return path_and_name_PDF

def main():

    img_type = "PNG"
    #total args
    #n=len(sys.argv)
    img_path = input('What is the absolute path of the file: ').strip('""')

    get_picture(img_path,img_type)





main()