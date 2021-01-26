#!/usr/bin/env python3

from io import BytesIO
from zipfile import ZipFile

def get_files(archive):
  is_file = lambda info: not info.is_dir()
  files = filter(is_file, archive.infolist())
  return [*files]


def main():
  metadata = []

  with ZipFile('./extra/archive.zip') as archive:
    for file in get_files(archive):
      with ZipFile(BytesIO(archive.read(file))) as flag_archive:
        for flag_file in get_files(flag_archive):
          crc = '0x%08x' % flag_file.CRC
          size = flag_file.file_size
          metadata.append((crc, size))

  print(repr(metadata).replace("'", ''))


if __name__ == '__main__':
  main()
