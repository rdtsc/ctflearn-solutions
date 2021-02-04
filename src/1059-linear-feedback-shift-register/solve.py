#!/usr/bin/env python3

from rng import make_rng

def main():
  with open('./extra/message.dat', 'rb') as file:
    rand = make_rng(11, (0, 2, 3, 5, 6))
    flag = ''.join(chr(c ^ rand()) for c in file.read())
    print(flag)


if __name__ == '__main__':
  main()
