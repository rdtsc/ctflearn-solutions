#!/usr/bin/env python3

import re

def decrypt(msg, key, lo=32, hi=95):
  return ''.join(chr((ord(c) + key - lo) % hi + lo) for c in msg)


def main():
  with open('./extra/image.jpg', 'rb') as file:
    file.seek(0x054a)
    msg = file.read(50).decode('ascii')

  flag_pattern = re.compile('(ctflearn{.*?})', re.IGNORECASE)

  for key in range(128):
    if flag := flag_pattern.search(decrypt(msg, key)):
      print(flag.group())
      break


if __name__ == '__main__':
  main()
