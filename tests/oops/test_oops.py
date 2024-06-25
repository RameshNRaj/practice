import unittest
from oops.oops import Grade

class TestOops(unittest.TestCase):

    def test_grading(self):
        grade = Grade()
        output = grade.main(20)

