
import random
import time

def main():
    introduction() #call the instructions function
    totalNumberOfCaves = 9 #set to the number of cave functions
    treasure = 50 #the initial amount of "treasure" the player has
    firstCave = 10 #initialize to a value that will not exist (cannot be between 0 and the total number of caves)
    secondCave = 10 #initialize to a value that will not exist (cannot be between 0 and the total number of caves)

    input("Press enter to begin: ")

    for x in range(3): #the loop will run 3 times, allowing the player to enter 3 caves
        #Call the choose cave function and save the returned value as caveNumber
        caveNumber = chooseCave(totalNumberOfCaves, firstCave, secondCave) 

        #Call the cave function for the given cave number
        #The returned value will be saved to treasure
        if caveNumber == 1:
            treasure = mushroom_Cave(treasure)
        elif caveNumber == 2:
            treasure = jewel_Cave(treasure)
        elif caveNumber == 3:
            treasure = turtle_Cave(treasure)
        elif caveNumber == 4:
            treasure = shinyCave(treasure)
        elif caveNumber == 5:
            treasure = stinkyCave(treasure)
        elif caveNumber == 6:
            treasure = moldyCave(treasure)
        elif caveNumber == 7:
            treasure = stinkycave(treasure)
        elif caveNumber == 8:
            treasure = rainbowcave(treasure)
        else:
            treasure = scarycave(treasure)
    
        #Save the cave number entered
        if x == 0:
            firstCave = caveNumber
        elif x == 1:
            secondCave = caveNumber
    
    #Give the user reasoning for why they will not enter another cave
    time.sleep(3)
    print("You notice the darkness at the cave entrance falling")
    print("and decide to take your treasure and go...")

    time.sleep(3)
    report(treasure)

def chooseCave(x, a, b):
    number = 0 #initialize the number variable

    #number == 0 allows the wile loop to begin
    #the loop continues until the number variable does not have the same value as a and b 
    #a and b get passed the values of firstCave and secondCave, so the user doesn't enter the same cave twice
    while number == 0 or number == a or number == b: 
        number = random.randint(1, x)

    return number #returns the number of the cave to be entered

def introduction():
    print()
    print("Welcome to Dragon's Realm!")
    print("Game Description:")
    print()
    print("\t1. In Dragon's Realm, you will travel along and encounter a variety caves")
    print("\t2. As the user, you get to choose three of the six caves to enter while on your journey")
    print("\t3. To start, you will be given 50 gold coins")
    print("\t4. Throughout your journey you will gain and lose coins as you encounter different caves")
    print("\t5. At the end of the game, you will leave either rich or broke") 
    print("\t6. Good luck!!") 
    print()

def mushroom_Cave(treasure):
    #cave number 1: mushrooms
    print ("You have encountered...")
    time.sleep(3)  #this basically pauses the program for 3 seconds (so text doesn't scroll past too fast)
    print("...A cave full of...mushrooms?")
    print("You are hungry so you decide to eat them...")
    lost = random.randint(1,11)
    treasure = treasure - lost
    print("Eating the mushrooms caused you to get sick! You had to use some coins for medicine.")
    print("You lost " + str(lost))
    print ("and you now have " + str(treasure)+ " gold coins!")
    print()
    return(treasure)

def jewel_Cave(treasure):
     #Cave number 3: jewels
    print ("You have encountered...")
    time.sleep(3)  #this basically pauses the program for 3 seconds (so text doesn't scroll past too fast)
    print("...A cave filled with Jewels!")
    print("A Jewel Bug comes into your periphrial vision! It attacks you!" )
    time.sleep(5)
    print("You dodge it and collect as many jewels as you can while running out of the cave!")
    gain = random.randint(1, 50)
    treasure= treasure + gain
    print("You are tired, but managed to escape with some Jewels and traded them for coins")
    print("You earned " + str(gain)+ " gold coins!")
    print ("and you now have " + str(treasure)+ " gold coins!") #How should we total all the coins, will other members give or take coins to the player? Talk about it in class tomorrow. 
    print()
    return treasure

def turtle_Cave(treasure):
     #Cave number 7: turtle cave
     print("You encounter...")
     time.sleep(4)
     print("A cave filled with turtles!")
     print("The turtles are tiny and cute. They make you feel happy.")
     time.sleep(5)
     print("You spend hours with the turtles and leave with happiness.")
     print("You gain no coins but have a lovely time.")
     print()
     return treasure

def shinyCave(treasure):
    print("You have encountered...")
    time.sleep(3)
    print("a cave full of crystals and jewels!")
    print("You found a pile of treasure in the corner...")
    treasure = treasure + random.randint(5, 15)
    print("You now have " + str(treasure) + " gold coins!")
    print()
    return treasure

def moldyCave(treasure):
    print("You have encountered...")
    time.sleep(3)
    print("a moldy, dark, damp cave. It smells like a basement.")
    print("(Which sort of smells like your grandma...)")
    time.sleep(3)
    print("Hurry! The mold is infecting your lungs!")
    box = int(input("There are three boxes, two of them containing oxygen masks. Choose between 1, 2, and 3!" ))
    if box == 1:
        print("You found an oxygen mask. Here's some treasure!")
        treasure = treasure + random.randint(1,5)
        print("You now have " + str(treasure) + " gold coins!")
    elif box == 2:
        print("You found an oxygen mask. Here's some treasure!")
        treasure = treasure + random.randint(1,5)
        print("You now have " + str(treasure) + " gold coins!")
    else:
        print("Darn... Nothing in this one.")
        print("You passed out from toxic fumes. When you woke up, some of your treasure is missing! ")
        treasure = treasure - random.randint(1,5)
        print("You now have " + str(treasure) + " gold coins!")
    print()
    return treasure

def stinkyCave(treasure):
    print("You have encountered...")
    time.sleep(3)
    print("a stinky, smelly, musty cave!")
    print("A goblin pops out of the darkness. He is mad you woke him up!")
    print("As punishment, he steals your treasure... ")
    treasure= treasure - random.randint(5,10)
    print ("You now have " + str(treasure)+ " gold coins.")
    print()
    return treasure

def stinkycave(treasure):
    #cave number 2: stinky
    print("You have encountered...")
    time.sleep(3)
    print("...the STINKY cave!")
    print("the stink disorients you, and a little goblin steals some of your treasure")
    treasure = treasure - random.randint(5,10)
    print ("and you now have " + str(treasure)+ " gold coins!")
    print()
    return(treasure)

def rainbowcave(treasure): 
    #cave number 3: rainbow
    print("You have now encountered... ")
    time.sleep(3)
    print("... the rainbow cave!")
    print("the air is smells sweet, and treasure falls from the sky!")
    treasure = treasure + random.randint(5,10)
    print ("you now have "  + str(treasure)+ " gold coins!")
    print()
    return(treasure)

def scarycave(treasure): 
    #cave number 4: sleepy
    print("You have now encountered... ")
    time.sleep(3)
    print("...the scary cave!")
    print("eyes peer at you from every angle, and suddenly fast and heavy footsteps approach")
    print("someone bumps into you, and steals some of your coins!")
    treasure = treasure + random.randint(5,10)
    print("and now you have " + str(treasure)+ " gold coins!")
    print()
    return(treasure)

def report(treasureLeft):
    if treasureLeft <= 50:
        print()
        print("Better luck next time... you're leaving broke!")
    elif treasureLeft > 50:
        print()
        print("Great job! You're leaving rich!")
    print()
    print("Thanks for playing, come back soon!")
    print()

main() #Call the main function