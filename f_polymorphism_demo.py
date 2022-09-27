# This program demonstrates polymorphism.

import f_animals as animals

def main():
    # Create a Mammal object, a Dog object, and
    # a Cat object.
    gorilla = animals.Mammal('gorilla')
    dog = animals.Dog()
    cat = animals.Cat()

    '''
    # Display information about each one.
    print('Here are some animals and')
    print('the sounds they make.')
    print('--------------------------')
    gorilla.show_species()
    gorilla.make_sound()

    show_mammal_info(creature): 

    print()

    dog.show_species()
    dog.make_sound()

    print()

    cat.show_species()
    cat.make_sound()

    '''

    show_mammal_info(gorilla)
    show_mammal_info(dog)
    show_mammal_info(cat)
    show_mammal_info('bird') #bird is a string so you get an error

def show_mammal_info(creature): 
    if isinstance(creature,animals.Mammal): #if creature is an instance of this class, then carry out the methods
        creature.show_species()
        creature.make_sound()
    else: 
        print(creature,"is not a mammal")
    
    #looking to see if an instance that you created belongs to a certain class
    #like
        #name = 'John'
        #if isinstance(name,string): #is name an instance of the string class 

# Call the main function.
main()
#make sound method changes based on the instance thats callin git

#attributes belonging to the superclass are not directly accessible by the sublcass

