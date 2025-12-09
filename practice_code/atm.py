Balance = 100000
B_Pin = 1234

print("----- Welcome to ATM -----")

while True:
    A = int(input("""
    To check balance enter 1
    To deposit enter 2
    To withdraw enter 3
    To exit enter 4
    Enter your choice: """))

    if A == 4:
        print("Thank you for using ATM!")
        break

    Pin1 = int(input("Enter your PIN: "))

    if Pin1 != B_Pin:
        print("Incorrect PIN, try again later!")
        continue
    else:
        print("Login Successfully!!!")

    
    if A == 1:
        print("You have Rs:", Balance, "in your account")

    
    elif A == 2:
        add_amount = int(input("Enter amount to deposit: "))
        Balance += add_amount
        print("Amount deposited successfully.")
        print("New Balance:", Balance)

    
    elif A == 3:
        withdraw_amount = int(input("Enter amount to withdraw: "))

        if withdraw_amount > 25000:
            print("You can withdraw maximum 25000 at a time.")

        elif withdraw_amount > Balance:
            print("Insufficient balance!")

        else:
            Balance -= withdraw_amount
            print("Withdrawal successful.")
            print("Remaining Balance:", Balance)

    else:
        print("Invalid choice. Please enter 1-4.")

    re_enter=input("Entre Yes/No :").lower()
    if(re_enter=="no" or "n"):
        break
    elif(re_enter=="yes" or "y"):
        continue
