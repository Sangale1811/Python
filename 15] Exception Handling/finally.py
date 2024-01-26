try:
    a=5//0
    print(a)

except ZeroDivisionError:
    print("Can't divide by zero")

finally:
    print("This is always executed")    
