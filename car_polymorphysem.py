class Ferrari:
    def model(self):
        print("The model is 488 GTB")
    def color(self):
        print("The color is Red")
    def year(self):
        print("The year it came out is 2023")

class BMW:
    def model(self):
        print("The model is X5")
    def color(self):
        print("The color is Black")
    def year(self):
        print("The year it came out is 2024")
obj_fer=Ferrari()
obj_bmw=BMW()
for car in (obj_fer, obj_bmw):
    car.model()
    car.color()
    car.year()
