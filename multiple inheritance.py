#This demo is for multiple inheritance
class Mysuperclass1:
    def method_super1(self):
        print("method_super1 method called")

class Mysuperclass2():
    def method_super2(self):
        print("method_super2 method called")


class Childclass(Mysuperclass1,Mysuperclass2):
    def child_method(self):
        print("This is child method")

c=Childclass()
c.child_method()
c.method_super1()
c.method_super2()
