import a_PlantClass as pc

primrose = pc.Plant("Green")
#creating a plant and setting the color to green
#primrose is an instance of the plant super class
sunflower = pc.Flower("Yellow",20)
#sunflower creating off of the sublcass called flower
#giving it the color yellow 
#need to give the petals because you are accessing a flower
    #added the 20 for the number of petals
print(primrose.get_color())

print(sunflower.get_color())
#sunflower is a subclass
#inherits the method color from the superclass (plant)
print(sunflower.get_petals())
#getpetals method belongs to the subclass

print(primrose.get_petals())
#super class does not access attributes of the sublcass so there would be an error with this
