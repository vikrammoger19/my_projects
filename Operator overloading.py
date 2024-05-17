class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, o):
        m1 = self.m1 + o.m1
        m2 = self.m2 + o.m2
        m3 = Student(m1, m2)
        return m3

    def __gt__(self, other):
        m1 = self.m1 + self.m2
        m2 = other.m1 + other.m2
        if m1 > m2:
            return True
        else:
            return False

    def __str__(self):
        return f"{self.m1},{self.m2}"


s1 = Student(58, 65)
s2 = Student(77, 49)

s3 = s1 + s2
print(s3.m2)

if s1 > s2:
    print("s1 wins")
else:
    print("s2 wins")

print(s1)
