#!/usr/bin/env python3

import re

def main():
  with open('./extra/image.jpg', 'rb') as file:
    data = file.read()

  for match in re.finditer(b'\xff\xfe', data):
    marker_end = match.end()
    data_start = marker_end + 2
    data_size = int.from_bytes(data[marker_end:data_start], 'big') - 2
    print('[Comment] 0x{:08x}: {:4} B'.format(data_start, data_size))


if __name__ == '__main__':
  main()
