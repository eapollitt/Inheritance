
class Athlete: #superclass three attributes
    def __init__(self,ht,wt,bodyfat):
        self.__ht = ht
        self.__wt = wt
        self.__bf = bodyfat

    def get_ht(self): #accessor methods
        return self.__ht

    def get_wt(self):
        return self.__wt

    def get_bf(self):
        return self.__bf



class Football_Player(Athlete): #special kind of athlete so getting more attributes only specific to a football player

    def __init__(self,ht,wt,bodyfat,position,team): #things we need to create the superclass

        Athlete.__init__(self,ht,wt,bodyfat) #initializing method of the super class is always the first thing you do

        self.__position = position #attributes only in the subclass
        self.__team = team


    def get_position(self):
        return self.__position

    def get_team(self):
        return self.__team










    
