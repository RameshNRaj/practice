class MeatPerson:
    def __init__(self):
        print('yes')

    def run(self, name):
        return f"Hello Boss, {name}!"

    def main(self):
        names = input("enter your name")
        meeting = self.run(names)
        return meeting


if __name__ == "__main__":
    meet_person = MeatPerson()
    meet_person.main()
