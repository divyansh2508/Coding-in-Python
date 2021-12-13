#This demo is for hierarchial inheritance
class Animal:
    def move(self):    #overriding
        print("I move therefore i am....")

class Human(Animal):
    def move(self):    #overriding
        print("Human can walk and run....")

class Fish(Animal):
    def move(self):    #overriding
        print("Fishes can swim and dive...")

i1=Animal()
i1.move()

h1=Human()
h1.move()

f1=Fish()
f1.move()
