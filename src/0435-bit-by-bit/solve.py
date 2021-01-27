#!/usr/bin/env python3

from base64 import b64decode
from re import search

def parse(data):
  data = b64decode(data).decode('ascii')
  op_start = search('\W', data).start()

  seq = [ord(c)**3 for c in data[:op_start]]
  ops = list(data[op_start:].replace('>>', '>').replace('<<', '<'))

  return seq, ops


def decode(data):
  seq, ops = parse(data)
  assert len(seq) - 1 == len(ops)

  result = seq[0]

  for i in range(len(ops)):
    for j in range(i, len(ops)):
      o = ops[j]
      n = seq[j + 1]

      if   o == '&': result &= n
      elif o == '^': result ^= n
      elif o == '|': result |= n
      elif o == '~': result = ~result
      elif o == '>': result >>= n
      elif o == '<': result <<= n

  return result


def main():
  flag = decode('YmluYXJ5cmVmaW5lcnl8JiY+PnxeXl4mJnx8fg==')
  print('CTFlearn{%s}' % flag)


if __name__ == '__main__':
  main()
