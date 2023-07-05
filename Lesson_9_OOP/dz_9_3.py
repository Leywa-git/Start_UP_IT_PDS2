class Parallelogram:
    def __init__(self, width=0, length=0):
        self.width = width
        self.length = length

    def get_area(self):
        s = self.width * self.length
        return print(s)


class Square(Parallelogram):
    def get_area(self):
        s = self.width * self.width
        return print(s)


parallelogram = Parallelogram(12, 20)
square = Square(12)

parallelogram.get_area()
square.get_area()
