#!/usr/bin/env python3

from secretsharing import PlaintextToHexSecretSharer as strategy

def main():
  with open('./extra/input.txt') as file:
    shares = (line.split() for line in file.readlines())
    shares = [f'{c[0]}-{c[2]}' for c in shares if c[0].isnumeric()]

  flag = strategy.recover_secret(shares)
  print('CTFlearn{%s}' % flag)


if __name__ == '__main__':
  main()
