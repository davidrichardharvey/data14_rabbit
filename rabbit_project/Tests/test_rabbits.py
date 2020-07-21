import unittest
from rabbit_project.sprint1 import Rabbit


class TestRabbits(unittest.TestCase):
    rab = Rabbit()

    def test_set_method(self):
        """
        _set_initial has inputs(months, males, females, male ages, female ages)
        It returns [total, months, number of females with starting age, number of males with starting age]
        """
        # Testing number of rabbits at initialisation
        self.assertEqual(self.rab._set_initial(0, 3, 3)[0], 6)
        self.assertEqual(self.rab._set_initial(0, 3, 3)[1], 0)
        self.assertEqual(self.rab._set_initial(1, 1, 1)[0], 2)
        self.assertEqual(self.rab._set_initial(1, 1, 1)[1], 1)

        # Tests the age of the rabbits at initialisation
        self.assertEqual(self.rab._set_initial(1, 1, 1, {3: 1}, {3: 1})[2], 1)
        self.assertEqual(self.rab._set_initial(1, 1, 3, {3: 1}, {3: 3})[3], 3)
        # Tests rabbit numbers are not None
        self.assertIsNotNone(self.rab._set_initial(4, 1, 1)[0])
        self.assertIsNotNone(self.rab._set_initial(2, 1, 1)[1])

