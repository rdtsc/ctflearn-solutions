#!/usr/bin/env python3

from binascii import unhexlify
from sympy import mod_inverse

def decode(msg):
  return unhexlify(format(msg, 'x')).decode('ascii')


def main():
  e = 3
  c = 219878849218803628752496734037301843801487889344508611639028
  n = 245841236512478852752909734912575581815967630033049838269083

  p = 416064700201658306196320137931
  q = n // p
  d = mod_inverse(e, (p - 1) * (q - 1))
  print('CTFlearn{%s}' % decode(pow(c, d, n)))


if __name__ == '__main__':
  main()
