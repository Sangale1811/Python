def Factorial(n):
    factorial=1
    if n==0:
        factorial = 1
    else:
        for i in range(1, n+1):
            factorial *= i

    return factorial

n=int(input("Enter n: "))

output=Factorial(n)
print("The factorial of ", n, "is", output)            



