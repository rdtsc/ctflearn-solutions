#!/usr/bin/env python3

def decode_digit_stream(digits):
  result = [0]

  for digit in map(int, digits):
    if not chr(result[-1]).isprintable():
      result[-1] *= 10
      result[-1] += digit
    else:
      result.append(digit)

  return result


def main():
  dtmf = decode_digit_stream('67847010810197110123678289808479718265807289125')
  print('CTFlearn{%s}' % ''.join(map(chr, dtmf)))


if __name__ == '__main__':
  main()
