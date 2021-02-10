#!/usr/bin/env python3

def main():
  values = [0x09, 0x1b, 0x11, 0x00, 0x16, 0x0b, 0x1d, 0x19, 0x17, 0x0e]
  values = zip(values, map(ord, 'CTFlearn{}'))

  for value in values:
    for i in range(128):
      if i ^ value[1] == value[0]:
        print(chr(i), value[0], chr(value[1]), sep='\t')
        break


if __name__ == '__main__':
  main()
