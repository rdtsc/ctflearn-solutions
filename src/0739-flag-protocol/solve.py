#!/usr/bin/env python3

from binascii import unhexlify

def main():
  order = unhexlify('14001813050b090810040d150203170f0a1106010e0712160c')
  value = unhexlify('64437d336175797b7465635f466c337030757254346e726d5f')
  flag = [chr(c) for _, c in sorted(zip(order, value))]
  print(''.join(flag))


if __name__ == '__main__':
  main()
