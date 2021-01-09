#!/usr/bin/env python3

'''
$ python3 -m pickletools extra/node.pickle | grep -io unicode.* | head -n10

UNICODE '__main__'
UNICODE 'Node'
UNICODE 'freq'
UNICODE 'data'
UNICODE '\x00'
UNICODE 'left'
UNICODE '9'
UNICODE 'right'
UNICODE '_count'
UNICODE '7'
'''

from pickle import load

class Node:
  pass


def main():
  with open('./extra/node.pickle', 'rb') as file:
    node = load(file)
    is_public = lambda prop: not prop.startswith('_')
    print(*filter(is_public, dir(node)))


if __name__ == '__main__':
  main()
