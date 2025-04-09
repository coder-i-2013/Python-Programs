from abc import ABC,abstractmethod
class animal:
    def move(self):
        pass
class Human(animal):
    def move(self):
        print("I wank and I run")
class snake(animal):
    def move(self):
        print("I slither")
class bear(animal):
    def move(self):
        print("I crawl with my 4 paws")
class kangaroo(animal):
    def move(self):
        print("I hop")

R= Human()
R.move()

S= snake()
S.move()

C= bear()
C.move()

H= kangaroo()
H.move()


