# Dictionaries are ordered collection of data items.
# This are key-value pairs that are separated by commas and enclosed within curly brackets.

my_info={'Name':'Shivani', 'Exam_No':'10', 'Branch':'Computer', 'Marks':[90, 87, 97, 98]}            # creating a dictionary
print(my_info)

print(my_info['Branch'])
print(my_info['Name'])

print(my_info.get('year'))     # If the key is not present in Dict then it will print None.

print(my_info.keys())          # it will print the all keys.
for key in my_info.keys():     
    print(my_info[key])        # gives the all values to the corresponding keys.

print(my_info.items())          # gives the key-value pairs.