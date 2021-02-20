#!/usr/bin/env python3

from binascii import unhexlify

def decode(msg):
  return unhexlify(format(msg, 'x')).decode('ascii')


def main():
  c = 9327565722767258308650643213344542404592011161659991421
  print('CTFlearn{%s}' % decode(c))


if __name__ == '__main__':
  main()
