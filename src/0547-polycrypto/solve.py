#!/usr/bin/env python3

import re
from binascii import unhexlify
from math import ceil

def chunkify(sequence, size):
  return [sequence[i:i + size] for i in range(0, len(sequence), size)]


def bits_to_string(bits):
  value = int(''.join(map(str, bits)), 2)
  return unhexlify('%x' % value).decode('ascii')


def main():
  with open('./extra/polynomial.txt') as file:
    values = re.sub('\D', ' ', file.read())
    values = [*map(int, values.split())]

  bit_count = ceil(max(values) / 8) * 8
  bits = [0] * bit_count

  for value in values:
    bits[value] = 1

  flag = bits_to_string(bits[::-1])
  print('CTFlearn{%s}' % flag)


if __name__ == '__main__':
  main()
