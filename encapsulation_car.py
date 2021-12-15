class car:
    __maxspeed=0
    __name=""
    def __init__(self):   #private
        self.__maxspeed=200
        self.__name="supercar"
    def drive(self):   #public
        print("Driving")
        print(self.__maxspeed)
        
    def setspeed(self,speed):   #public
        self.__maxspeed=speed
        print(self.__maxspeed)
        
redcar=car()   #object creation
redcar.drive()
redcar.setspeed(100)
