class Student:
    # --> Constructor Method
    def __init__(self, names, total_mark):
        self.total_marks = total_mark
        self.name = names

    ## Method
    def result(self):

        if self.total_marks > 50:
            return "pass"
        else:
            return "fail"

    ## Main Method
    def main(self):
        res = self.result()
        return name, res


## Inheritance
class Grade(Student):
    def __init__(self, names, total_mark):
        super().__init__(names, total_mark)
        self.total_marks = total_mark

    def main(self):
        if self.total_marks > 90:
            return "Grade A+"
        if 75 < self.total_marks < 90:
            return "Grade A"
        if 60 < self.total_marks < 75:
            return "Grade B"
        if 50 < self.total_marks < 60:
            return "Grade C"
        else:
            return "Grade D"


# control Statement
if __name__ == "__main__":
    # object
    name = input("enter your name")
    total_marks = int(input("enter your marks"))
    ## object
    student = Student(name, total_marks)
    student1 = student.main()
    grade = Grade(name, total_marks)
    grade1 = grade.main()
    print(student1)
    print(grade1)
