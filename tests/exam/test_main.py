
import unittest

from exam.main import MeatPerson


class TestMain(unittest.TestCase):
    def test_main(self):
        meat_person = MeatPerson()
        meat_person.main()
    # def test_run(self):
    #     meat_person = MeatPerson()
    #     self.assertEqual(meat_person.run('sample'), 'Hello Boss, sample!')
    #     # self.assertEqual(meat_person('Suresh'), 'Hello, Suresh!')


