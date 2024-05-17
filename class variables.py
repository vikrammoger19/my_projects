class computer:
    ram = 4
    core = "i5"  # local variable

    def __init__(self):
        self.camera = 8


c1 = computer()
print(c1.camera)
print(computer.core)
