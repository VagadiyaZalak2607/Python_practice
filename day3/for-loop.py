#name in loop
Name = "Zalak"
for i in Name:
    print(i)

#print numbers using for loop
num = [2,4,6,8,9,10,12,14,16,18,20,22,24,26]
for i in num:
    print(i)


#print table   
n = int(input("Enter n : "))

for i in range(1, 11):
    print(n, "*", i, "=", n * i)

#print numbers from 1 to 100
for i in range(0,100+1):
    print(i)


#print numberss from 100 to 1
for i in range(100,0,-1):
    print(i)


#pass statement
for i in range(5):
    pass

#sum of first n numbers
n = int(input("Enter n : "))
sum = 0
for i in range(1, n+1):
    sum += i
print("total sum =",sum)

#factorial of number using loop
n = int(input("Enter n : "))
factorial = 1
for i in range(1,n+1):
    factorial *= i

print("factorial is:",factorial)