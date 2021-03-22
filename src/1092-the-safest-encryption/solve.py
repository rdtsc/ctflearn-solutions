#!/usr/bin/env python3

import pdfplumber
from io import BytesIO
from zipfile import ZipFile

def main():
  with ZipFile('./extra/archive.zip') as archive:
    msg = archive.read('CTFLearn.pdf')
    key = archive.read('CTFLearn.txt')

  assert len(msg) == len(key)

  msg = bytes(a ^ b for a, b in zip(msg, key))

  with pdfplumber.open(BytesIO(msg)) as pdf:
    flag = pdf.pages[0].extract_text()

  print(flag.split()[-1])


if __name__ == '__main__':
  main()
