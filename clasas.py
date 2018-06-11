class complex:
    def __init__(self,x,y):
        self.a=x
        self.b=y
    def bca(self):
         num=[1,2,3,4,5,6,7,8]
         for nums in num:
            print(str(nums))
    def zz(self):
        numbers = [1,10,20,30,40,50]
        sum = 0
        for number in numbers:
             sum = sum + numbers
            print(sum)
x=complex(3,4)
print(x.a,x.b)
x.bca()
x.zz()