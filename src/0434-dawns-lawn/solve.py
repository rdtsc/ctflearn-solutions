#!/usr/bin/env python3

import numpy as np
from enum import IntEnum

class Entity(IntEnum):
  INFERTILE_DIRT = 0
  FERTILE_DIRT = 1
  GRASS_1 = 2
  GRASS_2 = 3
  GRASS_3 = 4
  GRASS_4 = 5
  FLOWER = 6


def unserialize(lawn):
  to_row = lambda row: [r'._\-/|*'.index(cell) for cell in row]
  lawn = np.array([to_row(line) for line in lawn.split()])
  assert lawn.shape[0] == lawn.shape[1]

  cells = lawn.T.copy()
  cells[1::2] = np.flip(lawn.T[1::2], 1)
  return cells.ravel(), lawn.shape[0]


def mow(lawn, growth_rate, trim_level=2):
  for i in range(len(lawn)):
    lawn[i] = max(lawn[i] - trim_level, 0)

    if lawn[i]:
      lawn[i] = min(lawn[i] + (len(lawn) - i) // growth_rate, Entity.FLOWER)


def main():
  with open('./extra/input.txt') as file:
    lawn, growth_rate = unserialize(file.read())
    mow(lawn, growth_rate)

  flag = sum(cell == Entity.FLOWER for cell in lawn)
  print('CTFlearn{%d}' % flag)


if __name__ == '__main__':
  main()
