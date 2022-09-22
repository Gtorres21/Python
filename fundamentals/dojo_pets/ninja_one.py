# from dojopets import pets

class Ninja():
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food


    def show_info(self):
        print(self.first_name, self.last_name,self.pet.name,self.treats,self.pet_food)

    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        self.pet.eat()
        return self

    def bathe(self):
        self.pet.noise()
        return self

# ralphael = Ninja("Ralphel", "Turle", splinter, "Cheese", "Pizza")

# ralphael.walk()