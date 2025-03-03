class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
         self.name = name
         self.owner = owner
         self.pet_type = pet_type
         type(self).all.append(self)
    @property
    def pet_type(self):
        return self._pet_type

    @pet_type.setter
    def pet_type (self,value):
        if value not in type(self).PET_TYPES:
            raise Exception(f"{value} is not a valid pet type.")
        self._pet_type = value

pet1 = Pet("Buddy", "dog", "Alice")
print(pet1.pet_type)
pet1.pet_type = "cat"
print(pet1.pet_type)

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner is self]
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise TypeError ("pet must be of type Pet")
        pet.owner = self


    def get_sorted_pets(self):
        return sorted([pet for pet in Pet.all], key=lambda pet: pet.name)

