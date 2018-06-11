class Person:
    def __init__(self,name,age,enrollno,branch):
        self.name=name
        self.age=age
        self.enrollno=enrollno
        self.branch=branch
p1 = Person("Riddham" , "21" , "0832cs15128","cse")
print("Name is "+p1.name)
print("Age is "+p1.age)
print("Enrollno is "+p1.enrollno)
print("Branch is "+p1.branch)