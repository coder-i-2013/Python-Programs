class Dog:
    def __init__(self,breed,name,age):
        self.breed=breed
        self.name=name
        self.age=age
Skippy= Dog("Black poodle mix","Skippy",70,)
print("Skippy was a {}".format(Skippy.breed))
print("{} was {} years old".format(Skippy.name,Skippy.age))

Chloe= Dog("Corgi","Chloe",21,)
print("\nChloe is a {}".format(Chloe.breed))
print("{} is {} years old".format(Chloe.name,Chloe.age))

Rider= Dog("Bernese Mountain","Rider",28,)
print("\nRider is a {}".format(Rider.breed))
print("{} is {} years old".format(Rider.name,Rider.age))

