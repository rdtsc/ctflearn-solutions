#!/usr/bin/env python3

from zipfile import ZipFile

def get_files(archive, unique = True):
  is_file = lambda info: not info.is_dir()
  files = filter(is_file, archive.infolist())

  if not unique:
    return [*files]

  crc_table = {}
  result = []

  for file in files:
    if file.CRC not in crc_table:
      result.append(file)
      crc_table[file.CRC] = True

  return result


def main():
  with ZipFile('./extra/image.jpg') as archive:
    lines = []

    for file in get_files(archive):
      lines.append('')
      lines.append(file.filename)
      lines.append('='*len(file.filename))
      try:
        lines.append(archive.read(file).decode('ascii').strip())
      except:
        lines.append('N/A')

    print('\n'.join(lines[1:]))


if __name__ == '__main__':
  main()
