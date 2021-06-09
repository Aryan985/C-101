import dropbox
class Transfer:
    def __init__(self,access_token):
        self.access_token = access_token
    def upload(self,From,to):
        dbx=dropbox.Dropbox(self.access_token)
        f = open(From,"rb")
        dbx.files_upload(f.read(),to)
def main():
    access_token = "LChXGXYtnWMAAAAAAAAAAY8cTcqOaOV_TOLdi2RZgUrCIKpCaZhyWjxYbcO9f8Ls"
    transfer = Transfer(access_token)
    From = input("Enter Path")
    to = input("Enter destination")
    transfer.upload(From,to)
    print("files Uploaded")
main()