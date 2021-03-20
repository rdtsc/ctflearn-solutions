#!/usr/bin/env python3

import re
from string import ascii_uppercase, octdigits

def extract(chunk):
  alpha = ascii_uppercase + octdigits[2:]
  chunk = ''.join('{:05b}'.format(alpha.index(c)) for c in chunk if c != '=')
  return re.findall('.{1,8}', chunk)[-1]


def main():
  with open('./extra/input.txt') as file:
    lines = [line.strip() for line in file.readlines()]

  flag = ''.join(extract(line[-8:]) for line in lines if line[-1] == '=')
  flag = [int(chunk, 2) for chunk in re.findall('.{1,8}', flag)]
  flag = ''.join(map(chr, filter(None, flag)))
  print('CTFlearn{%s}' % flag)


if __name__ == '__main__':
  main()
