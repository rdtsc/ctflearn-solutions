#!/usr/bin/env python3

import string
from io import BytesIO
from PIL import Image

def group(bits):
  groups = (''.join(map(str, bits[i:i+8])) for i in range(0, len(bits), 8))
  return bytearray(int(g, 2) for g in groups)


def get_first_non_printable_index(s):
  return next((i for i, c in enumerate(s) if c not in string.printable), None)


def main():
  with Image.open('./extra/image.png') as img:
    r_b1_lsb = group([r & 1 for r in img.getdata(0)])

  with Image.open(BytesIO(r_b1_lsb)) as img:
    r_b1_lsb = group([r & 1 for r in img.getdata(0)])

  flag = ''.join(map(chr, r_b1_lsb))
  flag_end = get_first_non_printable_index(flag)
  flag = flag[0:flag_end]

  print('CTFlearn{%s}' % flag)


if __name__ == '__main__':
  main()
