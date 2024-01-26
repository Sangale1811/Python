# Create an empty dictionary and add key-value pairs to it.
# Access values associated with specific keys in a dictionary.
# Update values of existing keys in the dictionary.
# Remove a key-value pair from a dictionary.
# Check if a key exists in a dictionary.

dict={}

# Add key-value pair in the dictionary
dict['name']='Shivani'
dict['roll_no']='61'
dict['branch']='computer'
dict['college_name']='PGMCOE'


# Access values associated with specific keys in a dictionary.
print(dict['name'])
print(dict['branch'])


# Update values of existing keys in the dictionary.
dict['roll_no']='79'
print(dict['roll_no'])


# Remove a key-value pair from a dictionary.
if 'roll_no' in dict:
    del dict['roll_no']
    print("'roll_no' key-value pair removed from dictionary")
else:
    print("'roll_no' key does not exist in the dictionary")    


# Check if a key exists in a dictionary.
if 'college_name' in dict:
    print(f"'college_name' key exists in the dictionary")
else:
     print(f"'college_name' key does not exist in the dictionary")    


