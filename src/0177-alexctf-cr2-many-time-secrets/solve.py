#!/usr/bin/env python3

from binascii import unhexlify

def decrypt(msg, key):
  key = map(ord, key)
  msg = zip(msg, key)
  return ''.join(chr(c[0] ^ c[1]) for c in msg)


def main():
  with open('./extra/input.txt') as file:
    lines = [unhexlify(line.strip()) for line in file.readlines()]

  dump = lambda: probe and print(*decrypt_all(), sep='\n')
  decrypt_all = lambda: [decrypt(line, flag) for line in lines]

  probe = False
  flag = 'ALEXCTF{'
  dump()

  flag = decrypt(lines[-1], 'ncryption scheme'); dump()
  flag = decrypt(lines[5], 'hod that is mathematically'); dump()

  print(flag)


if __name__ == '__main__':
  main()
