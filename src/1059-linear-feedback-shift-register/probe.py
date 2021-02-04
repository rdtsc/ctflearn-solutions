#!/usr/bin/env python3

from itertools import chain, combinations
from rng import make_rng

def brute(ciphertext, plaintext):
  assert len(ciphertext) >= len(plaintext)
  plaintext = [ord(c) for c in plaintext]
  schemas = [*chain.from_iterable(combinations(range(8), i) for i in range(8))]

  for seed in range(256):
    for schema in schemas:
      rand = make_rng(seed, schema)
      full_match = True

      for i in range(len(plaintext)):
        if ciphertext[i] ^ rand() != plaintext[i]:
          full_match = False
          break

      if full_match:
        return seed, schema

  assert False


def main():
  plaintext = 'CTFlearn{'

  with open('./extra/message.dat', 'rb') as file:
    ciphertext = file.read(len(plaintext))

  seed, schema = brute(ciphertext, plaintext)

  print('Seed:', seed)
  print('Schema:', schema)


if __name__ == '__main__':
  main()
