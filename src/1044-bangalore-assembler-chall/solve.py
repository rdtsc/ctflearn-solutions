#!/usr/bin/env python3

from data import payload

def main():
  decode = lambda c: chr((c[0] - c[4] ^ c[3]) - c[2] ^ c[1])
  print(*map(decode, payload), sep='')


if __name__ == '__main__':
  main()
