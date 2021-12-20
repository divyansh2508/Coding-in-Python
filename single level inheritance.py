#This demo is for Single level Inheritance
class Parent:
    def __init__(self):
        print("I am parent constructor")

    def display(self):
        print("I provide Black and White color")

class Child(Parent):
    def __init__(self):
        print("I am child constructor")
        super().__init__()


    def mymethod(self):
        print("Beep beep")

obj=Child()
obj1=Parent()
obj.display()
obj.mymethod()
input("Press any key to continue")
