class Rectangle:
    def __init__(self, length=0, width=0):
        self.length = length
        self.width = width

    def area(self):
        print(self.length * self.width)

tr_area = Rectangle(12, 12)
tr_area.area()