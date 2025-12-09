# 1 Write a program to take two numbers as input and print their sum.
a = int(input("Enter a Number1:"))
b = int(input("Enter a Number2:"))

print(f"sum of {a} and {b} is :",a+b)

# 2 Take a user's name and age as input and print a message: "Hello <name>, you are <age> years old!"
Name = str(input("Enter your Name:"))
Age = int(input("Enter your Age:"))
print(f"Hello!! {Name}, you are {Age} years old!")

# 3 Write a Python program to swap two numbers without using a third variable.
a = int(input("Enter first number a: "))
b = int(input("Enter second number b: "))

temp = a     
a = b       
b = temp     

print("After swapping:")
print("a =", a)
print("b =", b)


# 4 Swap two numbers without using a third variable

a = int(input("Enter first number a: "))
b = int(input("Enter second number b: "))

a = a + b
b = a - b
a = a - b

print("After swapping:")
print("a =", a)
print("b =", b)

# 5 Take a string input and print it in reverse.

str1 = str(input("Enter String: "))
reverse = "".join(reversed(str1))
print(reverse)

# Write a program to check whether a number is positive, negative, or zero.
a = int(input("Enter first number a: "))
if(a==0):
    print("number is zero")
elif(a>=0):
    print(f"{a} is positive")
elif(a<=0):
    print(f"{a} is negative ")

# Check if a given number is divisible by 5 and 11.
a = int(input("Enter first number a: "))
if(a%5&11==0):
    print(f"number{a}is divisible by 5 and 11")
elif(a%5==0):
    print(f"number{a}is divisible by 5")
elif(a%11==0):
    print(f"number{a}is divisible by 11")
else:
    print(f"number{a} is not diviisible by 5 and 11")

# Input a temperature in Celsius and convert it to Fahrenheit.
Temp = float(input("Enter first number Temp_celsius: "))
fahrenheit= (Temp * 9/5) + 32
print(f"{Temp}°C is = {fahrenheit}°F")

# Write a program to calculate the area of a circle.
Radius = float(input("Enter first number Radius: "))
Area = 3.14159 * Radius * Radius
print(f"area of circle is {Area}")

# Write a program to find the largest of three numbers.
a= int(input("Enter a number:"))
b= int(input("Enter a number:"))
c= int(input("Enter a number:"))
if(a>b and a>c):
    print("a is bigger")
elif(b>a and b>c):
    print("b is bigger")
else:
    print("c is bigger")

# Check whether a character is a vowel or consonant.
a1 = str(input("enter Vowel or Constant: "))
if(a1 == "a"):
    print(f"{a1} is vowel")
elif(a1=="e"):
    print(f"{a1} is vowel")
elif(a1=="i"):
    print(f"{a1} is vowel")
elif(a1=="o"):
    print(f"{a1} is vowel")
elif(a1=="u"):
    print(f"{a1} is vowel")
else:
    print(f"{a1} is constant")

# Write a program to check if a year is a leap year.
Year = int(input("Enter Year:"))
if(Year%4==0):
    print(f"{Year}is leap Year and it has 366 days")
else:
    print(f"{Year}is not leap Year and it has 365 days")

# Take marks of 3 subjects and print the grade:
sub1 = int(input("Enter a sub1:"))
sub2 = int(input("Enter a sub2:"))
sub3 = int(input("Enter a sub3:"))
Total_marks = sub1+sub2+sub3
Percentage = (Total_marks/300)*100
print(Total_marks)
print(Percentage)
if(Percentage>=90):
    print("grade A")
elif(Percentage>=80):
    print("grade B")
elif(Percentage>=70):
    print("grade C")
elif(Percentage>=60):
    print("grade D")
else:
    print("Fail")

# Print numbers from 1 to 100 using a loop.
i = 0
while(i<=100):
    print(i)
    i+=1
# Print the multiplication table of a number.
a= int(input("Enter a number:"))
for i in range(1,11):
    print(a,"*",i,"=",a*i)

a= int(input("Enter a number:"))
i = 0
while(i<=10):
    if(a<=0):
        print(f"{a} is not valid")
        break
    else:
        print(a,"*",i,"=",a*i)
        i+=1



# Print all even numbers between 1 and 50.

i=1
while(i<=50):
    if(i%2==0):
        print(f"{i} is even")
    i+=1

for i in range(1,50):
    if(i%2==0):
        print(f"{i} is even")
    else:
        pass
# Find the sum of the first N natural numbers.
n = int(input("Enter n : "))
sum = 0
for i in range(1, n+1):
    sum += i
print("total sum =",sum)

# Factorial of a number using loop.
n = int(input("Enter n : "))
factorial = 1
for i in range(1,n+1):
    factorial *= i

print("factorial is:",factorial)

#find greatest number using function
def gretest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
a = int(input("Enter A:"))
b = int(input("Enter B:"))
c = int(input("Enter C:"))
print(gretest(a,b,c))

#factorial using function
def factorial(n):
    if(n==0 or n==1):
        return 1
    return n * factorial(n-1)
n = int(input("Enter number:"))
print(factorial(n))

