Name = str(input("Enter your name:"))
IOT = int(input("IOT:"))
SPM = int(input("SPM:"))
MGD = int(input("MGD:"))
IWS = int(input("IWS:"))
Total_marks = IOT+SPM+MGD+IWS
Percentage = (Total_marks/200)*100
print(Name)
print(Total_marks)
print(Percentage)
if(Percentage>=90):
    print("grade A")
elif(Percentage>=70):
    print("grade B")
elif(Percentage>=50):
    print("grade C")
elif(Percentage>=30):
    print("grade D")
else:
    print("Fail")
   

