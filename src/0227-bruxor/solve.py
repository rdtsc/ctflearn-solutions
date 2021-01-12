#!/usr/bin/env python3

import re

def decrypt(string, key):
  return ''.join(chr(ord(c) ^ key) for c in string)


def main():
  for key in range(1, 127):
    flag = decrypt("q{vpln'bH_varHuebcrqxetrHOXEj", key)

    if re.search('{.*?}$', flag):
      print('CTFlearn{%s}' % flag)
      break


if __name__ == '__main__':
  main()
