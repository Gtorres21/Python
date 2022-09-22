from classes.character import Character


class Ninja(Character):

    def __init__( self , name ):
        super().__init__(name)
        self.name = name
        self.strength = 15
        # self.health = 100
    
    def shuriken_throw(self, target):
        dmg = self.strength*.1 + self.strength
        target.health = target.health - dmg
        print(f"{self.name} Throws his Ninja Star at {target.name} for {dmg}. {target.name} has {target.health} HP Left. ")
        return self

    # def show_stats( self ):
    #     print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    # def attack( self , pirate ):
    #     pirate.health -= self.strength
    #     print(f"{self.name} attacked {pirate.name}")
    #     return self