#!/usr/bin/env python3

from collections import Counter

def is_target_line(line):
  count = Counter(line)
  return count['0'] % 3 == 0 or count['1'] % 2 == 0


def main():
  with open('./extra/data.dat') as file:
    lines = file.read().splitlines()
    flag = sum(1 for _ in filter(is_target_line, lines))
    print(f'CTFlearn{{{flag}}}')


if __name__ == '__main__':
  main()
