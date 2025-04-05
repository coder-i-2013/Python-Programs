class My_class:
    __privateVar = 27
    def __privMath(self):
        print("I'm inside class myClass")
    def hello(self):
        print("private Variable value:",My_class.__privateVar)

foo= My_class()
foo.hello()
foo.__privMath()

