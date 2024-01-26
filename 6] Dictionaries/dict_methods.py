dict={'name':'Shivani', 'college':'PGMCOE', 'grades':'A'}
print(dict)

# update()
dict.update({'department':'Computer'})
print(dict)

# pop()
dict.pop('college')
print(dict)

# popitem() method removes the last key-value pair from the dictionary
dict.popitem()
print(dict)

# del
del dict['grades']
print(dict)

# clear()
dict.clear()
print(dict)