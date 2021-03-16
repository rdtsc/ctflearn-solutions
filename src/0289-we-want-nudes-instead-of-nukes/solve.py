#!/usr/bin/env python3

from binascii import unhexlify

def main():
  iv = unhexlify('391e95a15847cfd95ecee8f7fe7efd66')
  c = '8473dcb86bc12c6b6087619c00b6657e'

  c_plain = 'FIRE_NUKES_MELA!'.encode()
  c_poisoned = 'SEND_NUDES_MELA!'.encode()

  block_size = len(iv)
  poison = lambda i: iv[i] ^ c_plain[i] ^ c_poisoned[i]
  iv_poisoned = bytes(poison(i) for i in range(block_size))

  print('CTFlearn{flag{%s,%s}}' % (iv_poisoned.hex(), c))


if __name__ == '__main__':
  main()
