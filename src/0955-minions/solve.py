#!/usr/bin/env python3

from base64 import b64decode

def main():
  flag = b'VmtaU1IxUXhUbFZSYXpsV1RWUnNRMVpYZEZkYWJFWTJVVmhrVlZGVU1Eaz0='

  while not b'_' in flag:
    flag = b64decode(flag)

  print('CTFlearn{%s}' % flag.decode('ascii'))


if __name__ == '__main__':
  main()
