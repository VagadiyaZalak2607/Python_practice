print("---- Shopping Bill Calculator ----")
print("""
      cheese : 100
      milk : 50
      shampoo : 500
      wafers : 40
      biscuit : 30
      chocolates : 60
      ice cream : 70
""")

total = 0   

while True:
    item = input("Enter item name (or type 'done' to finish): ")

    if item == "done":
        break

    qty = int(input("Enter quantity: "))

    # price finder using simple if/elif
    if item == "cheese":
        price = 100
    elif item == "milk":
        price = 50
    elif item == "shampoo":
        price = 500
    elif item == "wafers":
        price = 40
    elif item == "biscuit":
        price = 30
    elif item == "chocolates":
        price = 60
    elif item == "ice cream":
        price = 70
    else:
        print("Item not found! Please enter correctly.")
        continue

    amount = price * qty
    total += amount
    print(item,"added : ",amount,"\n")

if total >= 1000:
    print("you get 10% discount")
    discount = (total * 10)/100
    # print("you get discount Rs:",discount) 
    # print("price before discount Rs:",amount) 
else:
    discount = 0

final_amount = total - discount

print("----- Final Bill -----")
print("price before discount Rs:",amount)
print("you get discount 10% Rs:",discount) 
print("Total Amount to pay Rs: ",final_amount)
