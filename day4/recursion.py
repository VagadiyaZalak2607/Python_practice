#recursion
def show(n):
    if(n==0):
        return 
    print(n)
    show(n-1)
n = int(input("enter n :"))
show(n)

 #factorial
def fact(n):
   if(n==0 or n==1):
      return 1
   else:
      return n * fact(n-1)
   
n = int(input("enter n :"))
print(fact(n))

#sun of first n natural numberss
def sum(n):
   if (n==0):
      return 0
   return sum(n-1)+n
n = int(input("enter n :"))
print(sum(n))



