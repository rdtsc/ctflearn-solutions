#!/usr/bin/env python3

from base64 import b64decode
from re import findall

def main():
  with open('./extra/data.pcap', 'rb') as file:
    dump = file.read().decode('utf8', errors='ignore')
    password = findall('pswrd=(\w+)', dump)[0] + '=='
    print('CTFlearn{%s}' % b64decode(password).decode('utf8'))


if __name__ == '__main__':
  main()
