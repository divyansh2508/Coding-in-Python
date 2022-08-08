def calc(r):
    import math
    peri=2*math.pi*r
    area=math.pi*r**2
    return peri,area

r=float(input("Enter the radius of the circle: "))
a,b=calc(r)
print("The area of circle is ",b)
print("The perimeter of the circle is",a)
