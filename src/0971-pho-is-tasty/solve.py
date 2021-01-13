#!/usr/bin/env python3

import string
from re import findall

def clean_header(header):
  is_char = lambda c: c in string.printable and c not in string.whitespace
  return ''.join(c for c in header if is_char(c))


def main():
  with open('./extra/image.jpg', 'rb') as file:
    payload = file.read(256).decode('ascii', 'replace')
    [flag] = findall('{(.*?)}', clean_header(payload))
    print('CTFlearn{%s}' % flag)


if __name__ == '__main__':
  main()
