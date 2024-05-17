class Polygon:

    def __init__(self):
        print("inside the constructor")

    # method to render a shape
    def render(self):
        print("Printing Polygon...")


class Square(Polygon):
    # renders Square
    def render(self):
        print("Printing Square...")


class Circle(Polygon):
    # renders circle
    def render(self):
        print("Printing Circle...")


# create an object of Square
s1 = Square()
s1.render()

# create an object of Circle
c1 = Circle()
c1.render()
