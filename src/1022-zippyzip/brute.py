from itertools import permutations
from zlib import crc32

def recover_plaintext(metadata, dictionary):
  target_crc, target_length = metadata

  for attempt in permutations(dictionary, target_length):
    if crc32(''.join(attempt).encode()) == target_crc:
      return ''.join(attempt)
