from mt19937predictor import MT19937Predictor

class Twister:
  def __init__(self, terms):
    self.__twister = MT19937Predictor()

    for term in terms:
      self.__twister.setrand_int32(term)

  def next(self):
    return self.__twister.genrand_int32()
