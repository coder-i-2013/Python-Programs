class A:
    def __init__(self,a):
        self.a=a
    def __lt__(self,other):
        if other.a<self.a:
            print("ob1 is greater than ob2")
        else:
            print("ob1 is greater than ob2")
    def __eq__(self,other):
        if other.a ==self.a:
            return("ob1 is equal to ob2")
        else:
            return("ob1 is not equal to ob2")
ob1=A(3)
ob2=A(2)
print("Values displayed: ",ob1.a,ob2.a)
print(ob1<ob2)

ob3=A(44)
ob4=A(44)
print("Values displayed: ",ob3.a,ob4.a)
print(ob3==ob4)