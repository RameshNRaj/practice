
class Student:
    # --> Constructor Method
    def __init__(self):
        pass

    ## Method
    def result(self, total_marks: int):

        if total_marks > 50:
            return "pass"
        else:
            return "fail"

    ## Main Method
    def main(self, name, total_mark):
        res = self.result(total_mark)
        return name, res


## Inheritance
class Grade(Student):
    def __init__(self):
        super().__init__()

    def grading(self, total_mark: int):
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

    def main(self, total_marks):
        res = self.grading(total_marks)
        return res


# control Statement
if __name__ == "__main__":
    # object
    name = input("enter your name")
    total_mark = int(input("enter your marks"))
    ## object
    obj = Student()
    obj1 = obj.main(name, total_mark)
    grad = Grade()
    grad1 = grad.main(total_mark)
    print(obj1)
    print(grad1)
