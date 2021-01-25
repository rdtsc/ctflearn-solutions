#!/usr/bin/env python3

from itertools import cycle

def decrypt(msg, key):
  key = cycle(key)

  def decode(c, k):
    a = ord('a' if str.islower(c) else 'A')
    b = (ord('A') * 2 + ord(c.upper()) - ord(k.upper())) % 26
    return chr(a + b)

  return ''.join(decode(c, next(key)) if str.isalpha(c) else c for c in msg)


def main():
  flag = decrypt('gwox{RgqssihYspOntqpxs}', 'blorpy')
  print('CTFlearn{%s}' % flag)


if __name__ == '__main__':
  main()
