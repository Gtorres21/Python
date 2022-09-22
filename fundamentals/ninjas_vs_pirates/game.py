from classes.pirate import Pirate
from classes.ninja import Ninja
import random





leonardo = Ninja("leonardo")
jack_Sparrow = Pirate("Jack Sparrow")



while(leonardo.health > 0 and jack_Sparrow.health > 0):
    # \n will add a line break
    response = input("You are Leonardo, will you attack or defend? \n 1) attack \n 2)special move \n 3)heal\n")
    if response == '1':
        leonardo.attack(jack_Sparrow)
    elif response == '2':
        leonardo.shuriken_throw(jack_Sparrow)
    elif response =='3':
        leonardo.heal()
    else:
        while(response != '1' and response != '2' and response != '3'):
            print("Please pick a valid option 1, 2 or 3")
            response = input("You are Leonardo, will you attack or defend? \n 1) attack \n 2)special move \n 3)heal\n")

    roll = random.randint(1,4)
    if roll == 1:
        jack_Sparrow.attack(leonardo)
    elif roll == 2:
        jack_Sparrow.pistol_shot(leonardo)
        
    elif roll == 3:
        jack_Sparrow.heal()
    elif roll == 4: 
        print(f"{jack_Sparrow.name} Stares in confusion and drinks rum")

    

        
if leonardo.health > 0:
    print("You beat a drunk pirate")
if jack_Sparrow.heal > 0:
    print("You've been defeated by a drunk pirate")
if leonardo.health <= 0 and jack_Sparrow.health <= 0:
    print("You both drank too much and are now friends")






















# leonardo.attack(jack_Sparrow)
# jack_Sparrow.pistol_shot(leonardo)


# leonardo.shuriken_throw(jack_Sparrow)
# leonardo.show_stats()
# jack_Sparrow.show_stats()
# jack_Sparrow.heal()






# michelangelo = Ninja("Michelanglo")

# jack_sparrow = Pirate("Jack Sparrow")

# michelangelo.attack(jack_sparrow)
# jack_sparrow.attack(michelangelo)
# michelangelo.show_stats()
# jack_sparrow.show_stats()