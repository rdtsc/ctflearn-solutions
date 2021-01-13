#!/usr/bin/env python3

def main():
  with open('./extra/message.txt') as file:
    symbols = file.read().strip()
    mapping = str.maketrans('!@#$%^&*()', '1234567890')
    symbols = map(int, symbols.translate(mapping).split(','))
    print('CTFlearn{%s}' % ''.join(chr(i) for i in symbols))


if __name__ == '__main__':
  main()
