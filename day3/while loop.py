#while loop

count = 1
while (count<=10):
    print("hello")
    count +=1

#print numbers from 1 to 50
i = 1
while(i<=50):
    print(i)
    i+=1

#reverse loop
i = 100
while(i>=1):
    print(i)
    i-=1

#table using while loop 
n = int(input("Enter n: "))
i = 1
while(i<=10):
    print(n*i)
    i+=1

#print numbers of list using loop
num = [2,4,6,8,10,12,14,15,16,18,20,22,24,26,28,30]
index = 0
while(index < len(num)):
    print(num[index])
    index+=1

#find specific element of list using loop
num = [2,4,6,8,10,12,14,15,16,18,20,22,24,26,28,30]
print(num)
i = 0
x = int(input("choose num from list:"))
while(i < len(num)):
    if(num[i]==x):
        print("found at index",i)
    i +=1

#continue
i = 0
while(i<=10):
    if(i%2==0):
        i+=1
        continue
    print(i)
    i+=1

    
