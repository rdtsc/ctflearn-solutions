#!/usr/bin/env python3

import re
from zipfile import ZipFile

def get_workers(archive):
  path = 'sources/android/support/constraint/BsdFKBmxbpWmGnzYUKFl.java'
  catalog = archive.read(path).decode('utf8')
  workers = re.findall('\.add\s*\(new\s+(.*?)\(', catalog)
  return [worker.split('.')[-1] for worker in workers]


def load_worker(archive, name):
  path = f'sources/de/vidar/run/a/{name}.java'
  source = archive.read(path).decode('utf8')

  order = re.search('private\s+long\s+.*?=\s*(.*?)\s*;', source)
  order = int(order.group(1))

  payload = re.search('private\s+char\s+.*?=\s*(.*?)\s*;', source)
  payload = payload.group(1)[1:-1].replace('\\', '')

  return order, payload, name


def decode(c, offset):
  a = ord('a' if str.islower(c) else 'A')
  return chr((ord(c) - a + offset) % 26 + a) if str.isalpha(c) else c


def main():
  with ZipFile('./extra/app.zip') as archive:
    workers = [load_worker(archive, name) for name in get_workers(archive)]

  msg = ''.join(decode(worker[1], 4) for worker in sorted(workers))
  flag = re.search('flag{.*?}', msg, re.IGNORECASE).group()
  print('CTFlearn{%s}' % flag)


if __name__ == '__main__':
  main()
