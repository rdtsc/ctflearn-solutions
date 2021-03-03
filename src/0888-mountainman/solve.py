#!/usr/bin/env python3

import os
import re

def brute(msg, pattern):
  for i in range(256):
    candidate = ''.join(chr(c ^ i) for c in msg)
    if pattern.match(candidate):
      return candidate


def main():
  with open('./extra/image.jpg', 'rb') as file:
    file.seek(-0x18, os.SEEK_END)
    flag = file.read(0x16)
    print(brute(flag, re.compile('CTF')))


if __name__ == '__main__':
  main()
