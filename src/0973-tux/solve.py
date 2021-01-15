#!/usr/bin/env python3

from zipfile import ZipFile

def main():
  with ZipFile('./extra/image.jpg') as archive:
    flag = archive.read('flag', b'Linux12345')
    print(flag.decode('ascii').strip())


if __name__ == '__main__':
  main()
