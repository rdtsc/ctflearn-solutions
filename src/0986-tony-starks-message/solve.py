#!/usr/bin/env python3

from base64 import b64decode
from pathlib import Path
from pickle import loads

class Node:
  pass


def get_encoding(path):
  def walk(node, result = {}, encoding = ''):
    if node.left or node.right:
      walk(node.left, result, encoding + '0')
      walk(node.right, result, encoding + '1')
    else:
      result[encoding] = node.data
    return result

  tree = loads(Path(path).read_bytes())
  return walk(tree)


def decode(message, encoding):
  result = []
  encoding = encoding.items()

  while message:
    decoded_chunk = False
    for code, char in encoding:
      if message.startswith(code):
        decoded_chunk = True
        result.append(char)
        message = message[len(code):]
        break
    assert decoded_chunk

  return b64decode(''.join(result)).decode('utf8')


def main():
  message = Path('./extra/data.txt').read_text().strip()
  encoding = get_encoding('./extra/node.pickle')
  print('CTFlearn{%s}' % decode(message, encoding))


if __name__ == '__main__':
  main()
