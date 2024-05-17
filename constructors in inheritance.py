class Student:
    def __init__(self):
        print("first constructor")


class Teacher:
    def __init__(self):
        # super().__init__()
        print("second constructor")


class Faculty(Teacher, Student):
    def __init__(self):
        super().__init__()
        print("Faculty constructor")




t = Faculty()
