Balance = 100000
print("----- Welcome to Python Bank -----")

A = float(input("""To check balance enter 1:
To deposit enter 2:
To withdraw enter 3:
to exit enter4:
Enter your choice: """))

if (A==1):
    print("you have RS:",Balance,"in your account")
elif(A==2):
    add_amount = float(input("Enter amount to deposit:"))
    Balance = Balance + add_amount
    print("you have RS:",Balance,"in your account")
elif(A==3):
    withdraw_amount = float(input("Enter amount to withdraw:"))
    if(withdraw_amount<25000):
        print("you can withdraw maximun 25000")
    elif(Balance<withdraw_amount):
        print("insufficient amount ")
    else:
        Balance = Balance - withdraw_amount
        print("you have RS:",Balance,"in your account")
elif A == 4:
    print("Thank you for using Python Bank!")
else:
    print(" Invalid choice. Please enter 1-4.")
