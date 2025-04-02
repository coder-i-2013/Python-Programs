class Vehichle:
    def __init__(self,max_speed,milage,name):
        self.max_speed=max_speed
        self.name=name
        self.milage=milage
class bus(Vehichle):
    pass

school_bus=bus(180,12,"Volvo")
print(" Vehichle: \n",school_bus.name,"\n Speed: \n", school_bus.max_speed,"\n Milage: \n",school_bus.milage,)
