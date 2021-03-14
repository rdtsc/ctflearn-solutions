#!/usr/bin/env python3

import csv
from collections import Counter

def main():
  with open('./extra/data.csv') as file:
    reader = csv.reader(file)
    columns = Counter()
    row_count = 0

    next(reader, None)
    for row in reader:
      row_count += 1
      for i, v in enumerate(row):
        columns[i] += float(v)

    mean = [int(columns[i] / (row_count - 1)) for i in sorted(columns.keys())]
    print(''.join(map(chr, mean)))


if __name__ == '__main__':
  main()
