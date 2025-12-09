username = "admin"
password = "1234"
Balance = 100000

for attempt in range(3+1):
    u = input("Enter username: ")
    p = input("Enter password: ")

    if u == username:
        if p == password:
            print("Login successful!")
            print("Your bank Balance is",Balance,"RS")
            break
        else:
            print("Incorrect Password! Try again.")
    else:
        print("Incorrect Username! Try again.")

else:
    print("Account locked! Too many attempts.")

