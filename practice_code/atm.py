Balance = 100000
B_Pin = 1234
print("----- Welcome to Python Bank -----")
while True:
    A = float(input("""To check balance enter 1:
    To deposit enter 2:
    To withdraw enter 3:
    to exit enter4:
    Enter your choice: """))

    if (A == 1):
        Pin1 = int(input("Enter your PIN: "))
        if(Pin1==B_Pin):
            print("you have RS:",Balance,"in your account")
        else:
            print("incorrect pin try again later")
    elif(A == 2):
        Pin1 = int(input("Enter your PIN: "))
        if(Pin1==B_Pin):
            add_amount = int(input("Enter amount to deposit:"))
            Balance = Balance + add_amount
            print("you have RS:",Balance,"in your account")
        else:
            print("incorrect pin try again later")
    elif(A ==3 ):
        Pin1 = int(input("Enter your PIN: "))
        if(Pin1==B_Pin):
            withdraw_amount = int(input("Enter amount to withdraw:"))
            if(withdraw_amount<25000):
                print("you can withdraw maximun 25000")
            elif(Balance<withdraw_amount):
                print("insufficient amount ")
            else:
                Balance = Balance - withdraw_amount
                print("you have RS:",Balance,"in your account")
        else:
            print("incorrect pin try again later")
    elif(A == 4):
        print("Thank you for using Python Bank!")
        break
    else:
        print(" Invalid choice. Please enter 1-4.")
