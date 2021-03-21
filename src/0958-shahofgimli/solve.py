#!/usr/bin/env python3

import tarfile
from hashlib import sha256
from io import BytesIO
from subprocess import PIPE, Popen

def decrypt(data, key, iv):
  cmd = f'openssl enc -d -aes-256-cbc -K {key} -iv {iv}'.split()
  cmd = Popen(cmd, stdin=PIPE, stdout=PIPE)
  return cmd.communicate(data)[0].decode('ascii')


def main():
  with open('./extra/image.jpg', 'rb') as file:
    file.seek(0x20517);
    tgz = file.read()

  with tarfile.open(fileobj=BytesIO(tgz)) as archive:
    key = archive.extractfile('Gimli04Base.jpg').read()
    msg = archive.extractfile('flag.enc').read()

  iv = '0' * 32
  key = sha256(key).hexdigest()
  print(decrypt(msg, key, iv))


if __name__ == '__main__':
  main()
