
class Plant:
    def __init__(self,color):
        self.__color = color
    #one attribute called color
    #received from the user

    def get_color(self):
        return self.__color
    #one method

class Flower(Plant):
    def __init__(self,color, petals):
        Plant.__init__(self,color)
    #sub class to plant
    #inherit plant as the superclass
    # in th einit method of the flower subclass, first thing is init method of pland
    #color and petals are two parameters from the suer
    #pass on color allows us to create the super class
    #petals do not apply to the plant, only to the flower sublcass
    #one way relationship - only works from the top down
    #flower sublcass can access the methods of the super class but the super class cannot access the methods of the sub class
    
        self.__petals = petals

    def get_petals(self):
        return self.__petals
