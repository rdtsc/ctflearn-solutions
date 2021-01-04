#!/usr/bin/env python3

def eval_unsafe(tokens):
  vm = [0]
  for token in tokens:
    if token == '-':
      vm[-1] -= 1
    elif token == '+':
      vm[-1] += 1
    elif token == '>':
      vm = vm[1:] + vm[:1]
    elif token == '<':
      vm = vm[-1:] + vm[:-1]
    elif token == '@':
      vm[-1], vm[-2] = vm[-2], vm[-1]
    elif token == '.':
      vm.append(vm[-1])
  return vm


def main():
  with open('./extra/input.txt') as file:
    tokens = list(file.read().strip())
    flag = ''.join(map(chr, eval_unsafe(tokens)))
    print(f'CTFlearn{{{flag}}}')


if __name__ == '__main__':
  main()
