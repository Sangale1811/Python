# Default Arguments
def average(a=4, b=10):
    print("The average is",(a+b)/2)

average(a=2)    



# Keyword Arguments
# The order in which the arguments are passed does not matter
def Full_Name(fName, mName, lName):
    print("Hii, ", fName, mName, lName)

Full_Name("Shivani", "Ramakant", "Sangale")



# Required arguments
def Addition(a,b,c=5):
    print("Addition of three number is : ", (a+b+c))

Addition(4,3)    



# Arbitary arguments (variable-length Arguments *args and **kwargs)
def addAllNumbers(*args):
    sum=0
    for i in args:
        sum+=i
    return sum

output=addAllNumbers(1, 2, 3, 4, 5)
print("The sum is: ", output)        
