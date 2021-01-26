#!/usr/bin/env python3

import string
from brute import recover_plaintext
from functools import partial
from multiprocessing import Pool

def main():
  flag_metadata = \
  [
    (0x21776b53, 4), (0xd3aa2e11, 4), (0x2788059e, 4),
    (0x657c5288, 4), (0xfc366b00, 4), (0x0315da00, 4),
    (0xf1cfb997, 4), (0xfc6b5b86, 4), (0x3cc92888, 4),
    (0xa6e14c90, 4), (0x5cf6c887, 4), (0xfc98a835, 4),
    (0xea80990c, 4), (0xfcb6e20c, 1)
  ]

  dictionary = '${_}' + string.digits + string.ascii_letters
  recover = partial(recover_plaintext, dictionary=dictionary)

  with Pool() as pool:
    flag = pool.map(recover, flag_metadata)

  print(''.join(flag))


if __name__ == '__main__':
  main()
