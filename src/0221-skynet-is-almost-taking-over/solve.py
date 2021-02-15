#!/usr/bin/env python3

from binascii import unhexlify
from data import e, c1, n1, n2
from sympy import gcdex, mod_inverse

def decode(msg):
  return unhexlify(format(msg, 'x')).decode('ascii')


def main():
  p = gcdex(n1, n2)[2]
  q = n1 / p
  d = mod_inverse(e, (p - 1) * (q - 1))
  print('CTFlearn{%s}' % decode(pow(c1, d, n1)))


if __name__ == '__main__':
  main()
