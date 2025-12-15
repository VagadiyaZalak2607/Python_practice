#operator overloading (when same operator have different meaning)
class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img

    def shownumber(self):
        print(self.real,"i +",self.img,"j")

    def __add__(self,num):
        newreal = self.real + num.real
        newimg = self.img + num.img
        return Complex(newreal, newimg)

num1 = Complex(1,3)
num1.shownumber()

num2 = Complex(3,1)
num2.shownumber()

num3 = num1 + num2
num3.shownumber()