import unittest
from oops.oops import Grade, Student


class TestOops(unittest.TestCase):

    def test_student(self):
        student = Student()
        self.assertEqual(student.main(51), "pass")
        self.assertEquals(student.main(45), "fail")

    def test_grading(self):
        grade = Grade()
        # output = grade.main(20)
        self.assertEquals(grade.main(91), "Grade A+")

    def test_grading1(self):
        grade = Grade()
        self.assertEquals(grade.main(80), "Grade A")

    def test_grading2(self):
        grade = Grade()
        self.assertEquals(grade.main(70), "Grade B")

    def test_grading3(self):
        grade = Grade()
        self.assertEquals(grade.main(55), "Grade C")

    def test_grading4(self):
        grade = Grade()
        self.assertEquals(grade.main(45), "Grade D")
