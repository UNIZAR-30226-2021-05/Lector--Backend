import dropbox
import os.path

DROPBOX_OAUTH2_TOKEN = 'Me56EUxeX0MAAAAAAAAAAXkCEw6O5oYINF1YCi5PoGZm9xjFhQxFswcp2o_Kla8L'
file_location = "/brainbook/"

dbx = dropbox.Dropbox(DROPBOX_OAUTH2_TOKEN)
def upload_file (file):
    with open(file,"rb") as f:
        dbx.files_upload(f.read(),file_location+file , mode=dropbox.files.WriteMode.overwrite)

def read_file (file):
    if os.path.isfile(file):
        print("File exist")
    else:
        print("File not exist")
        _, f =dbx.files_download(file_location+file)
        f=f.content
        f=f.decode("utf-8")
        print(f)