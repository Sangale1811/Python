a=[20,13,2,1,13,6]
print(a)

a.append(8)             # add an item to the end of the list       
print(a)

a.sort()                # sort the list in ascending order
print(a)

a.sort(reverse=True)     # sort the list in descending order
print(a)

a.reverse()
print(a)

print(a.index(13))       # return the index of first occurrence of the list item 

print(a.count(13))        # count number of item with given value

a.insert(2,7)                          # insert an item at the given index
print(a)

x=[70,80,90]
a.extend(x)
print(a)

