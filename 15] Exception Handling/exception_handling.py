a=input("Enter a Number : ")
print(f"Multiplication table of {a} is : ")

try:
    for i in range(1, 11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except:
    print("Invalid Input")

print("some imp lines of code")
print("End of Program")            