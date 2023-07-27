#My attempt at the solution
counter=0
i=int(input("Enter a number:"))

while i!=-1:
    counter+=1
    i=int(input("Enter a another number:"))
    average=(i/counter)
# I made the mistake of asking for an average too soon, of only the latest i interger rather than the sum.
    if i==-1:
# A break statement was also unnecessary because, in this instance, the print function would serve the same purpose.
        break
print(average)


#Solution provided by ChatGPT
counter = 0
i = int(input("Enter a number:"))
total = i
# What was required was a variable to contain the sum of intergers inputted to then be used in the calculation of the total average.

while i != -1:
    counter += 1
    i = int(input("Enter another number:"))
    if i != -1:
#Creating the sum of i inputs
        total += i

average = total / counter
print("The average of the", counter, "numbers entered is:", average)