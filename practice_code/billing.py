bill=0
total_item=[]
total_items=set()
while True:
    item=(input("Entre item name : "))
    price=int(input(f"Entre {item} price : "))
    quality=int(input(f"Entre the quality of {item} :"))
     
    bill+=quality*price
    discount=0

    if bill > 2000:
        discount = 20
    elif bill > 1000:
        discount = 10
 
    Total_bill=bill-((bill*discount)/100)
    total_item.append([item, quality, price,Total_bill])
    total_items.add(item)

    again_add=input("Entre the YES or NO to Add more value :").lower()
    if again_add == "no":
        break
    # total_item+=item
 
    
    for item, qty, price, amount in total_item:
        print(f"{item}: {qty} x {price} = {amount}")
print(f"your Item count {len(total_item)} ")
print(f"your Item is {(total_items)} ")
print(f"your item price is  {bill} ")
print(f"your discount is {discount} ")
print(f"your PAY amount is {Total_bill} ")