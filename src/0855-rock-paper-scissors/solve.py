#!/usr/bin/env python3

import re
import socket
import time

def play(hostname, port, moves, move_delay=0.5):
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.connect((hostname, port))
  moves = [*moves]
  response = b''

  while moves:
    sock.send(moves.pop(0).encode())
    time.sleep(move_delay)
    chunk = sock.recv(1024)
    if chunk == b'':
      break
    response += chunk

  sock.shutdown(socket.SHUT_RDWR)
  sock.close()
  return response


def get_winning_moves(opponent_moves):
  mapping = str.maketrans('RPS', 'PSR')
  return opponent_moves.translate(mapping)


def main():
  moves = get_winning_moves('RSRPRRPRSR')
  session = play('138.197.193.132', 5001, moves).decode('ascii')
  flag = re.search('ctflearn{.*?}', session, flags=re.IGNORECASE).group()
  print(flag)


if __name__ == '__main__':
  main()
