#!/usr/bin/env python3

from itertools import cycle

def main():
  flag = \
  [
    0x09, 0x1b, 0x11, 0x00, 0x16, 0x0b, 0x1d, 0x19, 0x17, 0x0b,
    0x05, 0x1d, 0x28, 0x05, 0x00, 0x35, 0x1b, 0x1f, 0x09, 0x2c,
    0x0d, 0x00, 0x18, 0x1c, 0x0e
  ]

  key = map(ord, 'jowls')
  flag = zip(flag, cycle(key))
  flag = ''.join(chr(c[0] ^ c[1]) for c in flag)
  print(flag)


if __name__ == '__main__':
  main()