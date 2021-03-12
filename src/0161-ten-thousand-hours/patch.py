import re

def chunk(fn):
  fn = re.sub('\[(\d+)', r'[-\1', fn)
  fn = re.sub('(\d+)\]', r'-\1]', fn)
  return fn


def digsub(fn):
  order = re.search("\[('\d+.*?)\]", fn)
  order = [*map(int, order.group(1).replace("'", '').split(','))]
  order = ','.join("'%d'" % order.index(i) for i in range(len(order)))
  return re.sub("\['\d+.*?\]", f'[{order}]', fn)


def shuffle(fn):
  order = re.search('\[(\d+,.*?)\]', fn)
  order = [*map(int, order.group(1).split(','))]
  order = ','.join(str(order.index(i)) for i in range(len(order)))
  return re.sub('\[\d+,.*?\]', f'[{order}]', fn)


def _replace(old, new):
  return lambda fn: fn.replace(old, new)


add = _replace('+', '-')
cadd = add
chadd = add

sub = _replace('-', '+')
csub = sub
chsub = sub

mul = _replace('*', '//')
cmul = mul
chmul = mul
