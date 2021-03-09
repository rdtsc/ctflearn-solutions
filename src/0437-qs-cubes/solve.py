#!/usr/bin/env python3

import re
from binascii import unhexlify
from collections.abc import Iterable
from itertools import cycle

def is_iterable(x):
  return isinstance(x, Iterable) and not isinstance(x, str)


def flat(x):
  if is_iterable(x):
    return [z for y in x for z in flat(y)]
  else:
    return [x]


def fold_down(cubes):
  midpoint = len(cubes) // 2
  top = cubes[:midpoint][::-1]
  btm = cubes[midpoint:]
  pile = []

  for i, row_top in enumerate(top):
    for j, col_top in enumerate(row_top):
      if is_iterable(col_top):
        col_top = col_top[::-1]
      top[i][j] = col_top

  for i, _ in enumerate(top):
    pile.append([*map(list, zip(top[i], btm[i]))])

  for i, row in enumerate(pile):
    if is_iterable(row[0]):
      for j, _ in enumerate(row):
        pile[i][j] = flat(pile[i][j])

  return pile


def fold_right(cubes):
  midpoint = len(cubes[0]) // 2
  pile = []

  for row in cubes:
    lhs = [v[::-1] for v in row[:midpoint]][::-1]
    rhs = row[midpoint:]
    pile.append([flat(v) for v in zip(lhs, rhs)])

  return pile


def fold(cubes, direction):
  direction = direction.strip().upper()[0]
  if direction == 'D':
    return fold_down(cubes)
  if direction == 'R':
    return fold_right(cubes)
  assert False


def main():
  with open('./extra/input.txt') as file:
    cubes = [[*line.strip()] for line in file.readlines()]

  for direction in cycle(['Down', 'Right']):
    if sum(len(v) for v in cubes) <= 1:
      break
    cubes = fold(cubes, direction)

  flag = ''.join(flat(cubes))
  flag = unhexlify(flag).decode('ascii')
  flag = re.search('try (\w+)', flag).group(1)
  print('CTFlearn{%s}' % flag)


if __name__ == '__main__':
  main()
