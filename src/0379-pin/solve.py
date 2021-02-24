#!/usr/bin/env python3

from subprocess import PIPE, Popen

def is_valid_pin(pin):
  app = Popen('./extra/pin', stdin=PIPE, stdout=PIPE)
  return b'salah' not in app.communicate(str(pin).encode())[0]


def main():
  for pin in (str(i) * j for i in range(9999) for j in range(1, 10)):
    if is_valid_pin(pin):
      print('CTFlearn{%s}' % pin)
      break


if __name__ == '__main__':
  main()
