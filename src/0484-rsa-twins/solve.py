#!/usr/bin/env python3

from binascii import unhexlify
from data import e, c, n, p
from sympy import mod_inverse

def decode(msg):
  return unhexlify(format(msg, 'x')).decode('ascii')


def main():
  q = n // p
  d = mod_inverse(e, (p - 1) * (q - 1))
  print('CTFlearn{%s}' % decode(pow(c, d, n)))


if __name__ == '__main__':
  main()
