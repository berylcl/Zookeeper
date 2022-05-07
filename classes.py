class Dog:
    # Class Object Attribute
    species = 'mammal'
    def __init__(self, breed,name,spots):
        self.breed = breed
        self.name = name
        self.spots = spots



sam = Dog(breed='Lab')
frank = Dog(breed='Huskie')
print(sam.breed)
print(type(sam))
