#print hello
print("Hello ")

#add two numbers
A = 22
B = 26
print("sum = ",A+B)

#find square root
N = int(input("Enter N: "))
square_root = N**0.5
print("square root of",N,"is: ",square_root)

#area of traingle
A = int(input("Enter side A:"))
B = int(input("Enter side B:"))
C = int(input("Enter side C:"))
Area = (A + B + C)/2
print("Area of triangle is : ",Area)

#number is Odd or Even
N = int(input("Enter Number:"))
if(N%2==0):
    print("Number is Even")
else:
    print("Number is Odd")

#number is positive or negative
N = int(input("Enter Number:"))
if(N>=0):
    print("Number is positive")
else:
    print("Number is Negative")

#year is leap year or not
Year = int(input("Enter Year:"))
if(Year%4==0):
    print(Year,"is leap Year and it has 366 days")
else:
    print(Year,"is not leap Year and it has 365 days")