# Import the datetime module and display the current date
import datetime

a = datetime.datetime.now()
print(a)

print(a.year)
print(a.strftime("%A"))
print(a.strftime("%B"))
