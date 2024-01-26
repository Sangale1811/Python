# Strings are immutable

a=" Shivani@@@ "
print(len(a))
print(a.upper())
print(a.lower())


# rstrip() removes any trailing characters
print(a.rstrip("@"))


# strip() removes any white spaces before and after the string
print(a.strip())


# replace() method replaces all occurences of string with another string
name="Silver Spoon"
print(name.replace("Sp","M"))


# split() method split the given string at specified instance and returns the separated strings as list items
str="Shivani Sangale"
print(str.split(" "))


# capitalize() method turns only the first character of the string to uppercase and rest other characters of the string are turned to lowercase.
# The string has no effect if the first character is already uppercase
Heading="introduction to React js"
print(Heading.capitalize())


# center() method align the string to the other as per the parameters given by the user
str1="Welcome to My Repository"
print(str1.center(50))


# count() method return the number of times the given value has occured within 
str1="AbcDeDrD"
print(str1.count("D"))


# endswith() method checks if the string ends with a given value. 
# If yes then return True, else return False
str1="Welcome to the console !!!"
print(str1.endswith("!!!"))
print(str1.endswith("t",3,12))


# find() method searches for the first occurence of the given value and return the index where it is present
# If the given value is absent from the string then return -1
str="Python is a programming language"
print(str.find("language"))


# index() method searches for the first occurences of given value and returns the index where it is present. 
# If the given value is absent from the string then raise an exception (ValueError: substring not found)
str="My Name is Shivani"
print(str.index("is"))     


# isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-9. If any other character orpunctuations are present, then it returns false
str="Hello123"
print(str.isalnum())


# isalpha() method returns True only if the entire string only consists of A-Z, a-z. If any other character or punctuations or numbers(0-9) are present, then it returns false
str="Hello"
print(str.isalpha())


# islower() method returns True if all the character in the string are lower case, else it return False
name="hii, i am shivani"
print(name.islower())


# isUpper() method returns True if all the character in the string are upper case, else it return False
name="HII, I AM SHIVANI"
print(name.isupper())


# isprintable() method return True if all the values within the given string are printable, if not, then return False.

# checking for printable characters 
string = 'My name is Shivani'
print(string.isprintable()) 
  
# checking if \n is a printable character 
string = 'My name is \n Shivani'
print(string.isprintable()) 
  
# checking if space is a printable character 
string = '' 
print( string.isprintable())


# isspace() method return True only and only if the string contains white spaces, else return False
str="         "
print(str.isspace())


# istitle() returns True only if the first letter of each word of the string is capitallized, else it return False
str="World Wide Web"
print(str.istitle())


# swapcase() method changes the character casing of the string, uppercase are converted to lowercase and lowwercase to uppercase
string="Python is a Interpreted Language"
print(string.swapcase())


# title() method capitalizes each letter of the word within the string.
str="She is very talented"
print(str.title())