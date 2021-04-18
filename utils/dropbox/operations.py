import dropbox
import textract
import os.path
import sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)))

DROPBOX_OAUTH2_TOKEN = 'Me56EUxeX0MAAAAAAAAAAXkCEw6O5oYINF1YCi5PoGZm9xjFhQxFswcp2o_Kla8L'
dropbox_file_location = "/brainbook/books/"
dropbox_image_location = "/brainbook/image/"
local_file_location = "../../libros/"
split_file=["titulo","tipo_fich"]


dbx = dropbox.Dropbox(DROPBOX_OAUTH2_TOKEN)
def upload_file (file):
    dropbox_file=file.rsplit("/",1)
    print(dropbox_file)
    with open(file,"rb") as f:
        dbx.files_upload(f.read(),dropbox_file_location+dropbox_file[1] , mode=dropbox.files.WriteMode.overwrite)

def read_file (file):
    split_file = file.split(".",1)
    txt_file = split_file[0]+"local.txt"
    if os.path.isfile(local_file_location+txt_file):
        print("File exist")
    else:
        print("File not exist")
        dropbox_file=open(local_file_location+file,"x")
        local_file = open (local_file_location+txt_file,'wb')
        dbx.files_download_to_file(local_file_location+file,dropbox_file_location+file)
        text=textract.process(local_file_location+file, method='pdfminer') 
        local_file.write(text)
        local_file.close()
        dropbox_file.close()
        os.remove(local_file_location+file)  

def upload_image (image):
    with open(image,"rb") as img:
        dropbox_file=image.rsplit("/",1)
        print(dropbox_file)
        dbx.files_upload(img.read(),dropbox_image_location+dropbox_file[1] , mode=dropbox.files.WriteMode.overwrite)

#def get_url (image):