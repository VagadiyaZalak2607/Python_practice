'''
Docstring for practice_code.game
1  = snake
-1 = water
0  = gun
'''
import random
you = int(input("Enter (1 for snake, -1 for water, 0 for gun): "))
computer = random.choice([1, -1, 0])  
print ("computer: ",computer)

if(computer == you):
    print("Match Draw!")

elif(computer == 1 and you == -1):  
    print("Computer Wins!")

elif(computer == -1 and you == 0):  
    print("Computer Wins!")

elif(computer == 0 and you == 1):  
        print("Computer Wins!")

else:
    print("You Win!!!")
