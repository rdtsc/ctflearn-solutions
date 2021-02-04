def make_rng(seed, schema):
  def rand():
    nonlocal seed
    msb = 0

    for n in schema:
      msb ^= (seed >> n) & 1

    seed = (seed >> 1) & ~(1 << 7) | (msb << 7)
    return seed

  return rand
