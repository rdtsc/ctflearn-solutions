#!/usr/bin/env python3

from base64 import b64decode
from re import findall

def layer3(msg):
  return ''.join([c[0] for c in msg.split('h4ck')][1:])


def layer2(msg):
  max_index = int(msg[4:6])
  pattern = ''.join('(.)%s' % i for i in reversed(range(max_index + 1)))
  payload = findall(pattern, msg[3:])[0]
  return ''.join(payload[::-1])


def layer1(msg):
  return b64decode(msg[19:-24])


def layer0(msg):
  return msg.decode('ascii')


def main():
  with open('./extra/message.txt') as file:
    flag = file.read().strip()

  for layer in [layer3, layer2, layer1, layer0]:
    flag = layer(flag)

  print('CTFlearn{%s}' % flag)


if __name__ == '__main__':
  main()
