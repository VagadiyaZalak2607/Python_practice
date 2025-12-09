# 1  = snake
# -1 = water
# 0  = gun

import random
you = int(input("Enter (1 for snake, -1 for water, 0 for gun): "))
if you not in [1, -1, 0]:
    print("Invalid choice! Enter only 1, -1, or 0.")
    exit()
else:
    computer = random.choice([1, -1, 0])  
    print ("computer: ",computer)

    if(computer == you):
            print("Match Draw!")

    elif(you == 1 and computer == -1):  
            print("You Win!!!")

    elif(you == -1 and computer == 0):  
            print("You Win!!!")

    elif(you == 0 and computer == 1):  
                print("You Win!!!")
    else:
            print("Computer Wins!!!")
