# for i in range(17):
#     if(i==12):
#         # print("skip the iteration")
#         continue
#     print("5 X ", i, "=", 5*i)



# Print odd numbers from 1 to 10 using continue
# for i in range(1, 11):
#     if i % 2 == 0:
#         continue  # Skip even numbers, move to the next iteration
#     print(i)



# Python program using a while loop to print numbers from 1 to 7 except for the number 4. Use the continue statement to skip printing the number 4.
i = 1

while (i <= 7):
    if (i == 4):
        i += 1
        continue  # Skip printing 4 and move to the next iteration
    
    print(i)
    i += 1

