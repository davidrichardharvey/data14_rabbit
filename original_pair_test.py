import unittest
from sprint1 import Rabbit

class PairTest(unittest.TestCase):

    rab = Rabbit()

    def test_original_par(self):
       # Tests that at start there are two rabbits, one male one female
       self.assertis((self.rab.months == 0), (self.rab.total == 2))
       self.assertis((self.rab.months == 0), (self.rab.number_males == 1))
       self.assertis((self.rab.months == 0), (self.rab.number_females == 1)
       # Tests rabbit numbers are not None
       self.assertIsNotNone(self.rab.total)
       self.assertIsNotNone(self.rab.number_males)
       self.assertIsNotNone(self.rab.number_females)