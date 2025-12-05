#function
def multiply(a, b):
    multiply = a*b
    print(multiply)
    return multiply
multiply(22,26)  

#average of 3 numbers
def average(a,b,c):
    sum = a+b+c
    average = sum/3
    print(average)
    return average
average(22,26,11)

#default parameter
def sum(a=1, b=1):
    sum = a+b
    print(sum)
    return sum
sum()

#length of list using function
list1 = ["ahmedabad","jesalmer","surat","banglore","mumbai","chennai"]
list2 = ["india","USA","UK"]
def len_list(list):
    print(len(list))
    return len

len_list(list1)
len_list(list2)

#factorial using function
def fact(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
        print(fact)
    return fact

n = int (input("Enter n:")) 
fact(n)

#convert dollar in indial rupee
def dollar_to_rupee(n):
    inr = n*83
    print(inr)
    return inr
n = int (input("Enter USD$:"))
dollar_to_rupee(n)

#num is even or odd
def even_odd(n):
    if(n%2==0):
        print(n,"is even")
    else:
        (n,"i odd")
    
    return n
n = int(input("Enter n: "))
even_odd(n)