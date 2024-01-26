# program to calculate factorial of number.
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)

print(factorial(5))            


# program to print the fibbonaci sequence.
def fibbonaci(n):
    if(n==0):                # base case
        return 0
    elif(n==1):               # base case
        return 1
    else:
        return fibbonaci(n-1)+fibbonaci(n-2)

print(fibbonaci(6))