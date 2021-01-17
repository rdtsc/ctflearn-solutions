#!/usr/bin/env python3

from base64 import b64decode
from brute import recover_password
from io import BytesIO
from zipfile import ZipFile

def main():
  with ZipFile('./extra/image.jpg') as main_archive:
    password = recover_password('e82a4b4a0386d5232d52337f36d2ab73')
    flag_zip = main_archive.read('flag.zip', bytes(password, 'ascii'))

  with ZipFile(BytesIO(flag_zip)) as flag_archive:
    flag = flag_archive.read('flag.txt')
    print('CTFlearn{%s}' % b64decode(flag).decode('ascii'))


if __name__ == '__main__':
  main()
