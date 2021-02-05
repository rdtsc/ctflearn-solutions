#!/usr/bin/env python3

from itertools import permutations
from multiprocessing import Pool, cpu_count

def normalize(notes):
  mapping = \
  {
    'G#': 'Ab', 'A#': 'Bb', 'Cb': 'B',
    'B#': 'C',  'C#': 'Db', 'D#': 'Eb',
    'Fb': 'E',  'E#': 'F',  'F#': 'Gb'
  }

  return [mapping[note] if note in mapping else note for note in notes.split()]


def chunkify(sequence, size):
  return (sequence[i:i + size] for i in range(0, len(sequence), size))


def is_octave(notes, keys):
  octave = [0, 2, 4, 5, 7, 9, 11, 12]
  scale = []

  for note in notes:
    i = keys.index(note) if note in keys else None

    if i is None:
      return False

    scale.append(i)
    keys[i] = ''

  return scale == octave


def is_major_scale(sequence):
  piano = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']
  shift = lambda n: piano[n:] + piano[:n] + [piano[n]]

  for notes in permutations(sequence):
    if notes[0] != notes[-1]:
      continue

    keys = shift(piano.index(notes[0]))

    if is_octave(notes, keys):
      return True

  return False


def brute(batch):
  return sum(is_major_scale(item) for item in batch)


def main():
  with open('./extra/input.txt') as file:
    samples = [*map(normalize, file.readlines())]
    samples = chunkify(samples, len(samples) // cpu_count())

  with Pool() as pool:
    flag = sum(pool.map(brute, samples))

  print('CTFlearn{%s}' % flag)


if __name__ == '__main__':
  main()
