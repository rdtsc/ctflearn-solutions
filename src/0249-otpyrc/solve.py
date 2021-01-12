#!/usr/bin/env python3

from binascii import unhexlify
from re import split

def unhex(fragment):
  return unhexlify(fragment).decode('ascii')


def main():
  msg = 'd733432373937303734373666343730373937323733343b7644534'
  lhs, rhs = split('{|}', unhex(msg[::-1]))[:2]
  flag = '%s{%s}' % (lhs, unhex(rhs))
  print('CTFlearn{%s}' % flag)


if __name__ == '__main__':
  main()
