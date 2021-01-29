#!/usr/bin/env python3

from binascii import unhexlify
from sympy import discrete_log

def get_private_key(public_key, prime=0x8c5378994ef1b, base=0x02):
  return discrete_log(prime, public_key, base)


def decode(key):
  return unhexlify(format(key, 'x')).decode('ascii')


def recover(public_key):
  return decode(get_private_key(public_key))


def main():
  a = recover(0x269beb3b0e968)
  b = recover(0x4757336da6f70)

  print('CTFlearn{%s_%s}' % (a, b))


if __name__ == '__main__':
  main()
