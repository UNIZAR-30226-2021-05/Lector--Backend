import dropbox
import textract
import os.path

DROPBOX_OAUTH2_TOKEN = 'Me56EUxeX0MAAAAAAAAAAXkCEw6O5oYINF1YCi5PoGZm9xjFhQxFswcp2o_Kla8L'
file_location = "/brainbook/books/"
image_location = "/brainbook/image/"
split_file=["titulo","tipo_fich"]


dbx = dropbox.Dropbox(DROPBOX_OAUTH2_TOKEN)
def upload_file (file):
    dropbox_file=file.rsplit("/",1)
    print(dropbox_file)
    with open(file,"rb") as f:
        dbx.files_upload(f.read(),file_location+dropbox_file[1] , mode=dropbox.files.WriteMode.overwrite)

def read_file (file):
    split_file = file.split(".",1)
    txt_file = split_file[0]+"local.txt"
    if os.path.isfile(txt_file):
        print("File exist")
    else:
        print("File not exist")
        dropbox_file=open(file,"x")
        open (txt_file,'wb')
        local_file = open(txt_file, "wb")
        dbx.files_download_to_file(file,file_location+file)
        text=textract.process(file, method='pdfminer') 
        local_file.write(text)
        local_file.close()
        dropbox_file.close()
        os.remove(file)  

def upload_image (image):
    with open(image,"rb") as img:
        dropbox_file=image.rsplit("/",1)
        print(dropbox_file)
        dbx.files_upload(img.read(),image_location+dropbox_file[1] , mode=dropbox.files.WriteMode.overwrite)

#def get_url (image):