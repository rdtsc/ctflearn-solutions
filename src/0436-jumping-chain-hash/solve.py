#!/usr/bin/env python3

def decode(c, offset):
  a = ord('a')
  return chr((ord(c) - a + offset) % 26 + a)


def sniff(msg, threshold=3):
  with open('/usr/share/dict/words') as file:
    words = sorted((word.strip() for word in file.readlines()), key=len)

  result = None

  for word in filter(lambda word: len(word) >= threshold, words):
    if word in msg:
      result = word

  return result, msg.index(result)


def main():
  with open('./extra/input.txt') as file:
    flag = ''.join(decode(c, 1) for c in file.read().strip())

  # print(sniff(flag), flag, sep='\n')
  print('CTFlearn{%s}' % flag[351:378])


if __name__ == '__main__':
  main()
