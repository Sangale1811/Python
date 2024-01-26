# class Details:
#     name="Shivani"
#     roll_no="61"

#     def info(self):
#         print("My Name is", self.name, "and roll no is", self.roll_no)

# obj1=Details()
# obj2=Details()

# obj2.name="Shiv"
# obj2.roll_no="87"

# obj1.info() 
# obj2.info()


class Student:

    def set_name(self, name):
        self.name=name         # class attribute

    def get_name(self):
        return self.name    

student1=Student()
student1.set_name("Shivani")
print(student1.get_name())

student1.math_mark=98       # instance attribute
print(student1.math_mark)

student2=Student()
student2.set_name("Sangale")
print(student2.get_name())