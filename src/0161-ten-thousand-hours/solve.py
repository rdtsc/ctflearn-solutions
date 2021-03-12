#!/usr/bin/env python3

import patch
import re
from types import ModuleType

def invert(functions):
  functions = functions.copy()
  patches = [fn for fn in dir(patch) if not fn.startswith('_')]

  for i, fn in enumerate(functions):
    for p in patches:
      if fn.startswith(f'def {p}_'):
        functions[i] = getattr(patch, p)(fn)
        break

  return functions


def load(app_path):
  with open(app_path) as file:
    lines = file.readlines()

  fn = []
  op = []

  for line in lines:
    if re.match('def\s|[ \t]', line):
      if line.startswith('def'):
        fn.append('$$$')
      fn.append(line.rstrip())

    elif re.match('flag\s*=\s*\w', line):
      op.append(line.split('=')[-1].split('(')[0].strip())

  if fn[0].startswith('$'):
    fn.pop(0)

  fn = invert([*map(str.strip, '\n'.join(fn).split('$$$'))])
  op.reverse()
  return fn, op


def build_app(functions):
  module = ModuleType('app')
  code = compile('\n'.join(functions), '<string>', 'exec')
  exec(code, module.__dict__)
  return module


def update_progress(msg=''):
  print('\x1b[1K\r', msg, sep='', end='', flush=True)


def main():
  with open('./extra/message.txt') as file:
    flag = [int(line.strip()) for line in file.readlines()]

  functions, steps = load('./extra/app.py')
  app = build_app(functions)
  app.k = len(flag)

  for i, step in enumerate(steps):
    update_progress('Deobfuscating: {:.1%}'.format(i / len(steps)))
    flag = getattr(app, step)(flag)

  update_progress()
  flag = ''.join(map(chr, flag))
  print('CTFlearn{%s}' % flag)


if __name__ == '__main__':
  main()
