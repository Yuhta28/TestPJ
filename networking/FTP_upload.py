import ftplib
import os

def upload(ftp, file):
    ext = os.path.splitext(file)[1]
    if ext in (".txt","html","htm"):
        ftp.storlines("STOR " + file, open(file))
    else:
        ftp.storbinary("STOR " + file, open(file, "rb"), 1024)

ftp = ftplib.FTP("127.0.0.1")
ftp.login("username", "password")
upload(ftp, "README.nluug")

# Test for AWS EC2