import requests
import sys

def uploadFile(file_to_upload):
    url = 'http://127.0.0.1:8000/upload/'
    myobj = {'file_uploaded': open(file_to_upload, 'rb')}
    x = requests.post(url, files=myobj)

    print(x.text)


if __name__ == "__main__":
    print(sys.argv[1])
    uploadFile(sys.argv[1])