class Student:
    # --> Constructor Method
    def __init__(self):
        pass

    ## Method
    def main(self, total_marks):
        if total_marks >= 50:
            return "pass"
        else:
            return "fail"


## Inheritance
class Grade(Student):
    def __init__(self):
        super().__init__()

    def main(self, total_mark):
        if total_mark > 90:
            return "Grade A+"
        if 75 < total_mark < 90:
            return "Grade A"
        if 60 < total_mark < 75:
            return "Grade B"
        if 50 < total_mark < 60:
            return "Grade C"
        else:
            return "Grade D"


# control Statement
if __name__ == "__main__":
    # object
    names = input("enter your name")
    total_marks = int(input("enter your marks"))
    ## object
    student = Student()
    student1 = student.main(total_marks)
    grade = Grade()
    grade1 = grade.main(total_marks)
    print(names)
    print(student1)
    print(grade1)
