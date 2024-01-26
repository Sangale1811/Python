# List are ordered collection of data items.
# They store multiple item in a single variables.
# List items are separated by commas and enclosed within square brackets [].

x = [2,4,5,3,"Shivani", True, False]
print(x)
print(type(x))
print(x[0])
print(x[1])

x[0]=1
print(x)

print(x[-3])             # slicing the list
print(x[1:7])
print(x[1:7:2])

# using "in" keyword
if "Shivani" in x:
    print("Yes")
else:
    print("No")    


# The in keyword is also used to iterate through a sequence in a for loop    
marks=[34,67,90,87]
for x in marks:
    print(x)