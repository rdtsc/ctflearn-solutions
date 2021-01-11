#!/usr/bin/env python3

def main():
  with open('./extra/message.txt') as file:
    msg = ''.join(str(int(ord(c) != 0x20)) for c in file.read())
    assert len(msg) % 8 == 0
    msg = ''.join(chr(int(msg[i:i+8], 2)) for i in range(0, len(msg), 8))
    print(msg.splitlines()[-1])


if __name__ == '__main__':
  main()
