#pattern using function
def pattern(n):
    if(n==0):
        return
    print("*"*n)
    pattern(n-1)
n = int(input("Enter number:"))
print(pattern(n))

#pattern 
def pattern(n):
    if(n==0 or n ==10):
        return
    print("*"*n)
    pattern(n+1)
n = int(input("Enter number:"))
print(pattern(n))

#pattern with count
def pattern(n):
    if(n==0):
        return
    print("1"*n,n)
    pattern(n-1)
n = int(input("Enter number:"))
print(pattern(n))

#square
def square(n):
    for i in range(n):
        print("*" * n)
n = int(input("Enter number:"))
print(square(n))
