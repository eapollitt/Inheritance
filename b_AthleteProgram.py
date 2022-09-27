import b_AthleteClass as ac

generic_athlete = ac.Athlete(6,220,0.2) #instance of superclass

quarterback = ac.Football_Player(6.2,250,0.15,'quarterback','offense') #also need posiiton and team
#instance of subclass

print("The height for the generic athlete is:",generic_athlete.get_ht())

#print("The team of the generic athlete is:",generic_athlete.get_team())
    #this one gives you an error because get_team is only part of the subclass not the super class athlete

#print("The team of the generic athlete is:",quarterback.get_team())
    #this one fixes it and runs fine
    
print("The weight for the football player is:",quarterback.get_wt())

print("The position of the football player is:",quarterback.get_position())
