#!/usr/bin/env python3

import base64

def get_fibonacci_terms(n):
  terms = [0, 1]

  for i in range(2, n):
    terms.append(terms[i - 1] + terms[i - 2])

  return terms


def main():
  lut = {}

  for index, value in enumerate(get_fibonacci_terms(128)):
    lut[value] = chr(index)

  with open('./extra/base.txt') as file:
    terms = base64.b64decode(file.read()).decode('ascii')
    terms = [lut[int(term)] for term in terms.split()]
    print('CTFlearn{%s}' % ''.join(terms))


if __name__ == '__main__':
  main()
