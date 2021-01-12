#!/usr/bin/env python3

from base64 import b64decode
from binascii import unhexlify

def unhex(fragment):
  return unhexlify(fragment).decode('ascii')


def layer0(msg, delimiter='.'):
  return msg[msg.index(delimiter)+1:].strip()


def layer1(msg):
  return b64decode(msg).decode('ascii')


def layer2(msg):
  return unhex(layer0(msg))


def layer3(msg):
  msg = layer0(msg).replace(' ', '')
  return unhex('%x' % int(msg, 2))


def layer4(msg):
  return layer1(layer0(msg, '!'))


def main():
  with open('./extra/message.txt') as file:
    flag = file.read()

  for layer in [layer0, layer1, layer2, layer3, layer4]:
    flag = layer(flag)

  print('CTFlearn{%s}' % flag)


if __name__ == '__main__':
  main()
