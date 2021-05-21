import dropbox
import os.path
from epub2txt import epub2txt
import sys
import tika
from tika import parser

sys.path.append(os.path.dirname(os.path.realpath(__file__)))

DROPBOX_OAUTH2_TOKEN = 'Me56EUxeX0MAAAAAAAAAAXkCEw6O5oYINF1YCi5PoGZm9xjFhQxFswcp2o_Kla8L'
dropbox_file_location = "/brainbook/books/"
dropbox_image_location = "/brainbook/image/"
local_file_location = "./libros/"
split_file=["titulo","tipo_fich"] 


dbx = dropbox.Dropbox(DROPBOX_OAUTH2_TOKEN)
def upload_file (file):
    dropbox_file=file.rsplit("/",1)
    print(dropbox_file)
    with open(file,"rb") as f:
        dbx.files_upload(f.read(),dropbox_file_location+dropbox_file[1] , mode=dropbox.files.WriteMode.overwrite)

def translate_file (file):
    split_file = file.split(".",1)
    txt_file = split_file[0]+"local.txt"
    if os.path.isfile(local_file_location+txt_file):
        #print("---------------------------->File exist")
        return  local_file_location+txt_file
    else:
        print("---------------------------->File not exist")
        local_file = open (local_file_location+txt_file,'w')
        print("---------------------------->local_file")
        print(split_file[1])
        if (split_file[1]=='pdf'):
            raw=parser.from_file(local_file_location+file)
            local_file.write(raw['content'])
        elif (split_file[1]=='epub'):
             local_file.write(epub2txt(local_file_location+file))
        else:
            dropbox_file=open(local_file_location+file)
            local_file.write(dropbox_file.read())
        local_file.close()
        os.remove(local_file_location+file)
        return  local_file_location+txt_file

def download_file(file):
    split_file = file.split(".",1)
    txt_file = split_file[0]+"local.txt"
    if ((os.path.isfile(local_file_location +file))or(os.path.isfile(local_file_location+txt_file))):
        return True
    else:
        dropbox_file=open(local_file_location+file,"x")
        print("---------------------------->dropbox_file")
        dbx.files_download_to_file(local_file_location+file,dropbox_file_location+file)
        print("---------------------------->Descargado")
        return True 

def upload_image (image):
    with open(image,"rb") as img:
        dropbox_file=image.rsplit("/",1)
        print(dropbox_file)
        dbx.files_upload(img.read(),dropbox_image_location+dropbox_file[1] , mode=dropbox.files.WriteMode.overwrite)

def get_url (image):
    aux = dbx.sharing_create_shared_link(dropbox_image_location+image)
    return  (aux.url).replace('www.dropbox.com','dl.dropboxusercontent.com')