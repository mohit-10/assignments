#1. Write a program which will find all such numbers which are divisible by 7 but are not amultiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.
result=[]
for x in range(2000, 3200):
    if (x%7==0) and (x%5!=0):
        result.append(str(x))
print (','.join(result))

#2. Write a Python program to accept the user's first and last name and then getting them printed in the the reverse order with a space between first name and last name.
first_name = input("Input your first name ")
last_name = input("Input your last name ")
print(last_name + " "+first_name)


#3. Write a Python program to find the volume of a sphere with diameter 12 cm.Formula: V=4/3 * π * r 3

diameter = 12
radius = diameter/2
volume = (4/3)*3.14*radius*radius*radius
print(volume)