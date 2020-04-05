#!/usr/bin/env python

class Car:
    def __init__(self):
        self.__updateSoftware()

    def drive(self):
        print("driving")

    def __updateSoftware(self):
        print("updating software")

redcar = Car()
redcar.drive()
#redcar.__updateSoftware() #not accesible from object.

# Private variables

class Car2:

    __maxspeed = 0
    __name = ""

    def __init__(self):
        self.__maxspeed = 200
        self.__name = "Supercar"

    def drive(self):
        print('driving. maxspeed ' + str(self.__maxspeed))

redcar = Car2()
redcar.drive()
redcar.__maxspeed = 10 # will not change variable because its private
redcar.drive()

# Settermethod
class Car3:

    __maxspeed = 0
    __name = ""

    def __init__(self):
        self.__maxspeed = 200
        self.__name = "Supercar"

    def drive(self):
        print('driving. maxspeed ' + str(self.__maxspeed))

    def setMaxspeed(self,speed):
        self.__maxspeed = speed

redcar = Car3()
redcar.drive()
redcar.setMaxspeed(320)
redcar.drive()
