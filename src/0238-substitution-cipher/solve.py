#!/usr/bin/env python3

from string import ascii_uppercase

def main():
  with open('./extra/message.txt') as file:
    msg = file.read().strip()

  mapping = str.maketrans('AZERTYUIOPQSDFGHNKLMWXCVBJ', ascii_uppercase)
  flag = msg.split('.')[0].translate(mapping).split()[-1]
  print('CTFlearn{%s}' % flag)


if __name__ == '__main__':
  main()
