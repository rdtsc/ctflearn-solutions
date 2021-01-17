from hashlib import md5

def recover_password(target_md5_digest):
  for i in range(0, 100000):
    password = 'ctflag' + str(i).zfill(5)
    digest = md5(password.encode('ascii')).hexdigest()

    if digest == target_md5_digest:
      return password

  assert False
