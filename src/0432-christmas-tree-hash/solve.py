#!/usr/bin/env python3

import re

def unserialize(data):
  data = data.strip().splitlines()
  data = [[*map(int, line.split())] for line in data]
  roots = data[0]
  tree = [[1]] + data[1:]
  return roots, tree


def traverse(tree):
  def explore(tree, depth=0, product=1):
    if depth < len(tree):
      for node in tree[depth]:
        term = product * node
        path.append(term)
        explore(tree, depth+1, term)

  path = []
  explore(tree)
  return path


def layer1(path, root):
  return [root * value for value in path]


def layer2(value):
  value = value.copy()
  stop = len(value) & ~1
  value[1:stop:2], value[:stop:2] = value[:stop:2], value[1:stop:2]
  return value[::-1]


def layer3(value):
  return ''.join(chr(n % 26 + ord('a')) for n in value)


def layer4(value):
  value = ''.join('{:b}'.format(ord(c)) for c in value)
  a = int(value[:16], 2)
  b = int(value[-16:], 2)
  return a & b


def layer5(value):
  value = re.findall('..?', str(value))
  return sum(map(int, value))


def layer6(value):
  return int(value) - (365**5 + 52**10 + 7**20 + 457981573849226022)


def layer7(value):
  value = map(int, re.findall('..?', str(value)))
  return layer3(value)


def main():
  with open('./extra/input.txt') as file:
    data = file.read()

  roots, tree = unserialize(data)
  path = traverse(tree)
  flag = ''

  for root in roots:
    value = layer1(path, root)
    value = layer2(value)
    value = layer3(value)
    value = layer4(value)
    value = layer5(value)
    flag += str(value)

  flag = layer6(flag)
  flag = layer7(flag)
  print('CTFlearn{%s}' % flag)


if __name__ == '__main__':
  main()
