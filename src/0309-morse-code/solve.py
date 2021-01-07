#!/usr/bin/env python3

morse = \
{
  '.-':   'A', '-...': 'B', '-.-.': 'C', '-..':  'D',
  '.':    'E', '..-.': 'F', '--.':  'G', '....': 'H',
  '..':   'I', '.---': 'J', '-.-':  'K', '.-..': 'L',
  '--':   'M', '-.':   'N', '---':  'O', '.--.': 'P',
  '--.-': 'Q', '.-.':  'R', '...':  'S', '-':    'T',
  '..-':  'U', '...-': 'V', '.--':  'W', '-..-': 'X',
  '-.--': 'Y', '--..': 'Z'
}

def main():
  with open('./extra/message.txt') as file:
    msg = (morse[code] for code in file.read().strip().split(' '))
    print('CTFlearn{%s}' % ''.join(msg))


if __name__ == '__main__':
  main()
