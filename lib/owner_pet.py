class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    all = []

    def __init__(self, name, pet_type, owner = 'Default'):
        self.name = name
        self.check_pet_type(pet_type)
        self._owner = owner
        Pet.all.append(self)

    def check_pet_type(self, pet_type):
        if pet_type in Pet.PET_TYPES:
            self.pet_type = pet_type
        else:
            raise Exception('Pet type is not in the accepted pet types.')
        
    @property
    def owner(self):
        return self._owner
    
    @owner.setter
    def owner(self, value):
        if isinstance(value, Owner):
            self._owner = value
        else:
            raise Exception('Owner type must be an instance of Owner.')
        

class Owner:
    def __init__(self, name):
        self.name = name

    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise Exception('Pet must be an instance of the Pet class.')
        
    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def get_sorted_pets(self):
        pets_list = [pet for pet in Pet.all if pet.owner == self]

        def sort_by_name(pet_item):
            return pet_item.name
        
        sorted_pets_list = sorted(pets_list, key = sort_by_name)
        return sorted_pets_list