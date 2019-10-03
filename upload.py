from ftplib import FTP
import sys

def upload_website(file):

    ftp = FTP('50.87.144.154', 'fabiange', 'gZmwG#HDlk0X')
    ftp.cwd('public_html/fabiangeiger.com')

    new_file = open(file, 'rb')
    ftp.storbinary(f'STOR {file}', new_file)
    new_file.close()


if __name__ == "__main__":

  file = sys.argv[1]

  upload_website(file)



