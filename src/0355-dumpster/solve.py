#!/usr/bin/env python3

from base64 import b64decode
from binascii import unhexlify
from Crypto.Cipher import AES

def main():
  key = unhexlify('075fde10a7aa496c80472b29642835e8')
  msg = b64decode('S+kUZtaHEYpFpv2ixuTnqBdORNzsdVJrAxWznyOljEo=')

  aes = AES.new(key, AES.MODE_ECB)
  msg = aes.decrypt(msg)
  msg = msg[0:-msg[-1]].decode('ascii')

  print('CTFlearn{%s}' % msg)


if __name__ == '__main__':
  main()
