import random
number = random.randint(1,100)
for attempt in range(3):
    G_num = int(input("Guess the number: "))
    if(G_num>number):
        print(G_num, "is to big")
    elif(G_num<number):
        print(G_num, "is to small")
    else:
        print(G_num,"is correct guess")
        break
else:
    print(f"Sorry! The correct number was {number}.")


