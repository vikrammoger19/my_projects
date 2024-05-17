# single level inheritance
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    pass


x = Student("Mike", "Olsen")
x.printname()

# multi level inheritance

class Family:
    def show(self):
        print("My Family....")


class Father(Family):
    name_father = ""

    def show1(self):
        print(self.name_father)


class Child(Father):
    name_child = ""

    def show2(self):
        print("Father Name :", self.name_father)
        print("Child Name : ", self.name_child)


o = Child()
o.name_father = "Sumit"
o.name_child = "Raja"
o.show()
o.show1()
o.show2()
