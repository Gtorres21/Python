class Ninja():
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        # super().__init__()
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

class Pet:
    def __init__(self, name, type, tricks, sound,owner=None):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 0
        self.energy = 0
        self.sound = sound
        self.owner = owner

        pass

    def sleep(self):
        self.energy = self.energy + 25
        return self
        
    def eat(self):
        self.energy = self.energy + 5
        self.health = self.health + 10
        print(f"{self.name} Eats some {self.owner.pet_food}. {self.name} raises his energy by {self.energy} and his health by {self.health}")
        return self

    def play(self):
        self.health = self.health + 5
        self.energy = self.energy - 5
        print(f"{self.name} Plays and gains {self.health} Health and has {self.energy} energy")
        return self

    def noise(self):
        print(f"{self.name} lets a out a loud {self.sound}")
        return self

splinter = Pet("Splinter", "Rat","wave","squeak")
ralphael = Ninja("Ralphel", "Turtle",splinter, "Cheese", "Pizza")
splinter.owner = ralphael




# ralphael.walk()
# ralphael.bathe()
ralphael.feed()

