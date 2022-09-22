# from dojopets import ninja_one


class Pet():
    def __init__(self, name, type, tricks, sound):
        super().__init__()
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 0
        self.energy = 0
        self.sound = sound

        pass

    def sleep(self):
        self.energy = self.energy + 25
        return self
        
    def eat(self):
        self.energy = self.energy + 5
        self.health = self.health + 10
        print(f"{self.name} Eats some {self.pet_food}. {self.name} raises his energy by {self.energy} and his health by {self.health}")
        return self

    def play(self):
        self.health = self.health + 5
        self.energy = self.energy - 5
        print(f"{self.name} Plays and gains {self.health} Health and has {self.energy} energy")
        return self

    def noise(self):
        print(f"{self.name} lets a out a loud {self.sound}")
        return self


    # splinter = Pet("Splinter", "Rat","wave","squeak")