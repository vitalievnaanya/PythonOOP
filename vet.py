class Vet:
    all_animals = []

    def __init__(self, name):
        self.name = name
        self.animals = []
        self.space = 5

    def register_animal(self, animal_name):
        if self.space <= len(self.all_animals):
            return f'Not enough space'
        self.animals.append(animal_name)
        self.all_animals.append(animal_name)
        return f'{animal_name} registered in the clinic'

    def unregister_animal(self, animal_name):
        if animal_name not in self.all_animals:
            return f'{animal_name} not in the clinic'
        self.all_animals.remove(animal_name)
        self.animals.remove(animal_name)
        return f'{animal_name} unregistered successfully'

    def info(self):
        return f'{self.name} has {len(self.animals)} animals. {self.space - len(self.all_animals)} space left in clinic'


peter = Vet("Peter")
george = Vet("George")
print(peter.register_animal("Tom"))
print(george.register_animal("Cory"))
print(peter.register_animal("Fishy"))
print(peter.register_animal("Bobby"))
print(george.register_animal("Kay"))
print(george.unregister_animal("Cory"))
print(peter.register_animal("Silky"))
print(peter.unregister_animal("Molly"))
print(peter.unregister_animal("Tom"))
print(peter.info())
print(george.info())