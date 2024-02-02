# Implement exception handling in python by showing division operation
# You can show exception - "ZeroDivisionError"


a=int(input("Enter a: "))
b=int(input("Enter b: "))

try: 
    result=a/b

except ZeroDivisionError:
    result=None
    print("Error: Cannot Divide by Zero")

finally:
    print("Division operation completed: ", result)
