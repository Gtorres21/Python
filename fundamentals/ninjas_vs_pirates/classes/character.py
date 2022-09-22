class Character:

    def __init__(self, name):
        self.name = name
        self.strength = 10
        self.health =  100

    # def show_stats( self ):
    #     print(f"Name: {self.name}\nStrength: {self.strength}\nHealth: {self.health}\n")

    def attack ( self , target ):
        target.health = target.health - self.strength
        print(f"{self.name} attacked {target.name}. {target.name} has {target.health} HP Left. We have {self.health} HP Left")
        return self

    def heal (self):
        self.health = self.health + 4
        print(f"{self.name} heals for 4 now has {self.health} HP")


