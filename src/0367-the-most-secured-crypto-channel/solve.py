#!/usr/bin/env python3

from base64 import b64decode
from pathlib import Path

def get_transmission(id):
  return Path(f'./extra/transmission{id}.txt').read_text().strip()


def polarization_to_bits(polarization):
  mapping = str.maketrans(r'\|/-', '1100')
  return polarization.translate(mapping)


def decode(bits):
  groups = (''.join(map(str, bits[i:i+8])) for i in range(0, len(bits), 8))
  return ''.join(chr(int(g, 2)) for g in groups)


def main():
  alice_polarization = get_transmission(1)
  alice_matches = get_transmission(3)

  alice_bits = polarization_to_bits(alice_polarization)
  secret = filter(lambda q: q[1] == 'v', zip(alice_bits, alice_matches))
  secret = decode(''.join(q[0] for q in secret))
  flag = b64decode(secret.split(':')[-1]).decode('ascii')

  print('CTFlearn{%s}' % flag)


if __name__ == '__main__':
  main()
