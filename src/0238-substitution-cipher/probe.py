#!/usr/bin/env python3

import re
from cipher_solver.simple import SimpleSolver

def decrypt(msg, method='random'):
  solver = SimpleSolver(msg)
  solver.solve(method)
  return (solver.plaintext(), solver.decryption_key())


def main():
  with open('./extra/message.txt') as file:
    msg = file.read().strip()

  while True:
    flag = decrypt(msg)
    txt = flag[0].split('.')[0]
    key = flag[1].upper()

    if re.search('flag is.*like', txt, re.IGNORECASE):
      print(f'key: {key}')
      print(f'txt: {txt}')
      break


if __name__ == '__main__':
  main()
