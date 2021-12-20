class Student:
    def __init__(shruti,n,a,m):    #constructor
        shruti.name=n
        shruti.age=a
        shruti.marks=m

    def display(shruti):
        print("Hello my name is",shruti.name)
        print("My age is",shruti.age)
        print("My percentile is",shruti.marks) 

    
st=Student("Divyansh",17,85)
st.display()

st1=Student("Shruti",17,95)
st1.display()
