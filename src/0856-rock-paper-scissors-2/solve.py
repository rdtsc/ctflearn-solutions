#!/usr/bin/env python3

import re
import socket
from twister import Twister

def update_progress(msg=''):
  print('\x1b[1K\r', msg, sep='', end='', flush=True)


def collect_mt_terms(sock, count=624, default_response='R'):
  terms = []

  while len(terms) < count:
    update_progress('Collecting terms: {:.1%}'.format(len(terms) / count))

    chunk = sock.recv(1024)
    reply = chunk.decode('ascii')

    if 'choose' in reply:
      sock.send(default_response.encode())
      if term := re.search('on (\d+)', reply):
        terms.append(int(term.group(1)))

  sock.send(default_response.encode())
  assert len(terms) == count
  return terms


def play(hostname, port):
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.connect((hostname, port))

  response = ''
  twister = Twister(collect_mt_terms(sock))

  update_progress('Playing...')

  while True:
    sock.send('PSR'[twister.next() % 3].encode())
    chunk = sock.recv(1024)
    reply = chunk.decode('ascii')
    response += reply

    if '{' in reply:
      break

  update_progress()
  sock.shutdown(socket.SHUT_RDWR)
  sock.close()
  return response


def main():
  session = play('138.197.193.132', 5002)
  flag = re.search('ctflearn{.*?}', session, flags=re.IGNORECASE).group()
  print(flag)


if __name__ == '__main__':
  main()
