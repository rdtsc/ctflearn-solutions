#!/usr/bin/env python3

def decode(msg):
  to_index = lambda chunk: [n - 1 for n in map(int, chunk.split('-'))]
  to_chunk = lambda chunk: to_index(chunk) if len(chunk) > 1 else chunk
  to_char = lambda yx: 'ABCDEFGHIJLMNOPQRSTUVWXYZ'[5 * yx[0] + yx[1]]

  msg = map(to_chunk, msg.split(','))
  msg = [to_char(chunk) if type(chunk) is list else chunk for chunk in msg]

  return ''.join(msg)


def main():
  msg = '1-3,4-4,2-1,{,4-4,2-3,4-5,3-2,1-2,4-3,_,4-5,3-5,}'
  print('CTFlearn{%s}' % decode(msg))


if __name__ == '__main__':
  main()
