#!/usr/bin/env python3

from re import findall

bacon = \
{
  'AAAAA': 'A', 'AAAAB': 'B', 'AAABA': 'C', 'AAABB': 'D',
  'AABAA': 'E', 'AABAB': 'F', 'AABBA': 'G', 'AABBB': 'H',
  'ABAAA': 'I', 'ABAAB': 'K', 'ABABA': 'L', 'ABABB': 'M',
  'ABBAA': 'N', 'ABBAB': 'O', 'ABBBA': 'P', 'ABBBB': 'Q',
  'BAAAA': 'R', 'BAAAB': 'S', 'BAABA': 'T', 'BAABB': 'U',
  'BABAA': 'W', 'BABAB': 'X', 'BABBA': 'Y', 'BABBB': 'Z'
}

def main():
  with open('./extra/message.txt') as file:
    msg = (bacon[code] for code in findall('.{5}', file.read().strip()))
    print('CTFlearn{%s}' % ''.join(msg))


if __name__ == '__main__':
  main()
