class Rectangle:
    def __init__(self, height, width):
        self.height=height
        self.width=width

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return (self.height + self.width) * 2

rectangle=Rectangle(4, 3)   

print("The height and width are:", rectangle.height, rectangle.width)
print("Area:", rectangle.area())
print("Perimeter:", rectangle.perimeter())
