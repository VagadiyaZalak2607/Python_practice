Number1= int(input("Enter Num1:"))
Number2= int(input("Enter Num2:"))
Operator= input("Enter Operator(+,-,*,/,%):")
if(Operator=="+"):
    print(Number1,Operator,Number2,"=",Number1+Number2)
elif(Operator=="-"):
    print(Number1,Operator,Number2,"=",Number1-Number2)
elif(Operator=="*"):
    print(Number1,Operator,Number2,"=",Number1*Number2)
elif(Operator=="/"):
    print(Number1,Operator,Number2,"=",Number1/Number2)
elif(Operator=="%"):
    print(Number1,Operator,Number2,"=",Number1%Number2)
else:
    print("Enter valid Operator")
