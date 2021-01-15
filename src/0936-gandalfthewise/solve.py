#!/usr/bin/env python3

import string
from base64 import b64decode

def clean_header(header):
  header = [c for c in header if c in string.printable or c == '\n']
  header = ''.join(header).splitlines()
  return [b64decode(s[1:]) for s in header if s.startswith('+')]


def main():
  with open('./extra/image.jpg', 'rb') as file:
    payload = file.read(256).decode('ascii', 'replace')
    a, b = clean_header(payload)
    assert len(a) == len(b)

  flag = ''.join(chr(a[i] ^ b[i]) for i in range(len(a)))
  print('CTFlearn{%s}' % flag)


if __name__ == '__main__':
  main()
