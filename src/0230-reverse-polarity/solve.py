#!/usr/bin/env python3

def main():
  with open('./extra/data.txt') as file:
    bits = file.read().strip()
    values = (bits[i:i+8] for i in range(0, len(bits), 8))
    values = map(lambda n: chr(int(n, 2)), values)
    print('CTFlearn{%s}' % ''.join(values))


if __name__ == '__main__':
  main()
