class Student:
    school = "Telusko"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    # instance method
    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3

    @classmethod
    def info(cls):
        return cls.school

    @staticmethod
    def get_school():
        print("this is static method")


c1 = Student(34, 45, 65)
c2 = Student(45, 64, 76)

print(c1.avg())
print(Student.info())
Student.get_school()
