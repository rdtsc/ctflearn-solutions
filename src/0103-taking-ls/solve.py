#!/usr/bin/env python3

from pathlib import Path
from re import findall
from zipfile import ZipFile

def main():
  with ZipFile('./extra/archive.zip') as archive:
    password = archive.read('The Flag/.ThePassword/ThePassword.txt')
    [password] = findall('"([^"]+)"', password.decode('ascii'))
    flag = archive.read('The Flag/The Flag.pdf', bytes(password, 'ascii'))
    Path('./flag.pdf').write_bytes(flag)
    print('PDF Password: "%s"' % password)


if __name__ == '__main__':
  main()
