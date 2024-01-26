class Rectangle:

    def set_dimensions(self, height, width):
        self.height=height
        self.width=width

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return (self.height + self.width) * 2

rectangle=Rectangle()

height_input=int(input("Enter the height: "))
width_input=int(input("Enter the width: "))

rectangle.set_dimensions(height_input, width_input)

print("The height and width are: ", rectangle.height, rectangle.width)
print("The area is: " , rectangle.area())
print("The Perimeter is: ", rectangle.perimeter())




   