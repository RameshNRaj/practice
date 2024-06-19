
import unittest

from exam.main import MeatPerson


class TestMain(unittest.TestCase):
    def test_user(self):
        meat_person = MeatPerson()
        self.assertEqual(meat_person.run('sample'), 'Hello Boss, sample!')
        # self.assertEqual(meat_person('Suresh'), 'Hello, Suresh!')



