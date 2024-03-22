game = "Raf's Text Based Dungeon Crawler Demo"
print("Hi! Welcome to", game + ". What's your name?")
reqAge = 18
name = input()
validAge = False
while not validAge:
    print("...and how old are you? ")
    age = input()
    if age.isdigit():
        validInt = True
        break
    else:
        print('The input is not a valid number. Please restart the game.')
        exit()
if int(age) >= reqAge:
    print("That works for me! Good luck", name + "!")
else:
    print("Oof... You will have to wait", reqAge - int(age), "year(s) before you can play.")

# define player variables:

HP = 10
physicalpower = 1
magicalpower = 1
#inventory and encountered as list
inventory = []
encountered = []
#equip as singular variable
equip_left = ''
equip_right = ''
equip_ring = ''

# define utility functions
def health_checker():
    global HP
    print("your total health is: " + str(HP))
    if HP == 0:
        print("Game Over bruv")
        quit()

def character_info():
    global HP
    global physicalpower
    global magicalpower
    magicalpower = 1
    physicalpower = 1
    if equip_ring == "Ring of Power":
        magicalpower += 1
        physicalpower += 1
    print("your total health is: " + str(HP))
    print('Your physical power is: ' + str(physicalpower))
    print('Your magical power is: ' + str(magicalpower))

def game_info():
    print("Welcome in the dungeon, if you want to manage equipment, type 'equipment' whenever you are prompted with a choice. You can do the same for statistics and HP by typing 'character'. Type 'info' for necessary game information in case you forget")


def equip_stuff():
    global inventory
    global equip_ring
    global equip_left
    global equip_right
    if inventory == []:
        print("empty inventory, returning")
        return
    else:
        print("Welcome in the equipment window: Your inventory contains: " + ' ,'.join(inventory))
        print("Your current equipment is: \n left hand: " + str(equip_left) + "\n right hand: " + str(equip_right) + "\n ring slot: " + str(equip_ring))
        print("will you equip something? Spells are equipped in your left hand, swords and daggers in your left. Two-handed weapons will require both")
        inventory.append("no")
        userInput = ""
        while userInput not in inventory:
            print("please input item name or no")
            userInput = input()
            if userInput == "Ring of Power" and "Ring of Power" in inventory:
                equip_ring = "Ring of Power"
                print("equipped Ring of Power in ring slot")
            elif userInput == "Ring of Power" and "Ring of Power" not in inventory:
                print("You do not have this item")
            elif userInput == "bonemeal":
                print("cannot equip bonemeal")
            elif userInput == "no":
                print("Nothing was equiped")
            else:
                print("You should have learned how to type by now, try a different input")
        inventory.remove("no")
def powercalculator():
    # this function is called before each fight to calculate power numbers according to your equipment
    global magicalpower
    global physicalpower
    global equip_ring
    global equip_left
    global equip_right
    magicalpower = 1
    physicalpower = 1
    if equip_ring == "Ring of Power":
        magicalpower += 1
        physicalpower += 1
    print("your magical power is: " + str(magicalpower))
    print("your physical power is: " + str(physicalpower))


# dungeon functions (rooms)
# by design, I would do it like this: offer choices that lead to different functions. these functions can be other rooms, fights, etc.



def EnteringTheDungeon():
    directions = ["left","right","forward"]
    print("Welcome in the dungeon, if you want to manage equipment, type 'equipment' whenever you are prompted with a choice. You can do the same for statistics and HP by typing 'character'. Type 'info' in case you forget game details. Feel free to try it out now! \nYou find yourself in the entrance hall of this mysterious ancient place. You can choose to go down any of the four halways, where will you go?")
    userInput = ""
    while userInput not in directions:
        print("Please input: left/right/backward/forward")
        userInput = input()
        if userInput == "left":
            RingOfPowerRoom()
        elif userInput == "right":
            FightingSkeletonsRoom1()
        elif userInput == "forward":
            DiningHallRoom()
        elif userInput == "backward":
            print("Don't pussy out, your journey has only just begun")
        elif userInput == "equipment":
            equip_stuff()
        elif userInput == "character":
            character_info()
        elif userInput == "info":
            game_info()
        else:
            print("You should have learned how to type by now, try a different input")

def ReturnEnteringTheDungeonFromRing():

    directions = ["right","forward"]
    print("You slip the Jade Ring in your pocket and feel the weight of its power. You walk back into the entrance hall of this mysterious ancient place.")
    print("You can choose to go down any of the four halways, where will you go?")
    userInput = ""
    while userInput not in directions:
        print("Please input: left/right/backward/forward")
        userInput = input()
        if userInput == "left":
            print("You've been there already, greedy cunt")
        elif userInput == "right" and "skeletons1fight" in encountered:
            print("You have already bravely fought in this room")
            userInput = ""
        elif userInput == "right" and "skeletons1flight" in encountered:
            print("you were so scared before, your knees tremble and your fear keeps you from entering")
            userInput = ""
        elif userInput == "right":
            FightingSkeletonsRoom1()
        elif userInput == "forward":
            DiningHallRoom()
        elif userInput == "backward":
            print("Don't pussy out, your journey has only just begun")
        elif userInput == "equipment":
            equip_stuff()
        elif userInput == "character":
            character_info()
        elif userInput == "info":
            game_info()
        else:
            print("You should have learned how to type by now, try a different input")

def ReturnEnteringTheDungeonFromSkeleton():
    global encountered
    directions = ["left","forward"]
    print("You whipe the grime from your face after that scary encounter. You walk back into the entrance hall of this mysterious ancient place.")
    print("You can choose to go down any of the four halways, where will you go?")
    userInput = ""
    while userInput not in directions:
        print("Please input: left/right/backward/forward")
        userInput = input()
        if userInput == "left" and "ringroom" in encountered:
            print("You've been there already, greedy cunt")
            userInput = ""
        elif userInput == "left" and "ringroom" not in encountered:
            RingOfPowerRoom()
        elif userInput == "right" and "skeletons1flight" in encountered:
            print("you were so scared before, your knees tremble and your fear keeps you from entering")
        elif userInput == "right" and "skeletons1fight" in encountered:
            print("You have already bravely fought in this room")
        elif userInput == "forward":
            DiningHallRoom()
        elif userInput == "backward":
            print("Don't pussy out, your journey has only just begun")
        elif userInput == "equipment":
            equip_stuff()
        elif userInput == "character":
            character_info()
        elif userInput == "info":
            game_info()
        else:
            print("You should have learned how to type by now, try a different input")

def RingOfPowerRoom():
    global encountered
    choices = ["pick up","leave"]

    print("You find yourself in a brightly lit empty room, with a pedestal in the center that contains a Jade ring, what will you do?")

    userInput = ""
    while userInput not in choices:
        print("please input: pick up / leave")
        userInput = input()
        if userInput == "pick up":
            inventory.append("Ring of Power")
            encountered.append("ringroom")
            ReturnEnteringTheDungeonFromRing()
        elif userInput == "leave":
            encountered.append("ringroom")
            EnteringTheDungeon()
        elif userInput == "equipment":
            equip_stuff()
        elif userInput == "character":
            character_info()
        elif userInput == "info":
            game_info()
        else:
            print("You should have learned how to type by now, try a different input")

def FightingSkeletonsRoom1():
    global HP
    global physicalpower
    global magicalpower
    global encountered
    choices = ["fight","flight"]
    print("the stench of rotten flesh overcomes you as you see two sets of glowing eyes in the darkest corner of the room, what will you do?")
    userInput = ""
    while userInput not in choices:
        print("please input: fight / flight")
        userInput = input()
        if userInput == "flight":
            print("You manage to escape but are struck in the back by an arrow, -2HP")
            HP -= 2
            health_checker()
            encountered.append("skeletons1flight")
            ReturnEnteringTheDungeonFromSkeleton()
        elif userInput == "fight":
            print("Two Skeletons emerge from the dark")
            powercalculator()
            if physicalpower > 1 or magicalpower > 1:
                print("easily overcome, no damage taken")
                encountered.append("skeletons1fight")
                print("added bonemeal to your inventory")
                inventory.append("bonemeal")
            else:
                print("a hard fight, you won, but take 1 HP damage")
                HP -= 1
                health_checker()
                encountered.append("skeletons1fight")
                print("added bonemeal to your inventory")
                inventory.append("bonemeal")
            ReturnEnteringTheDungeonFromSkeleton()
        elif userInput == "equipment":
            equip_stuff()
        elif userInput == "character":
            character_info()
        elif userInput == "info":
            game_info()
        else:
            print("You should have learned how to type by now, try a different input")

def DiningHallRoom():
    global HP
    global physicalpower
    global magicalpower
    global inventory
    choices = ["forward", "fire"]
    print("You enter a large dining hall and the door shuts behind you. There's an open flame pit in the middle, what will you do?")
    inventory.append("nothing")
    userInput = ""
    burninput = ""
    while userInput not in choices:
        print("You can keep walking, or sit by the fire. \n please input: forward / fire")
        userInput = input()
        if userInput == "forward":
            lastroom()
        elif userInput == "fire":
            print("you sit by the fire, please select an item to burn: ")
            print(inventory)
            while burninput not in inventory:
                burninput = input()
                if burninput == "nothing":
                    "You burn nothing and continue"
                    lastroom()
                elif burninput == "Ring of Power":
                    "You cannot burn this item, burn anything else?"
                    burninput = ""
                elif burninput == "bonemeal":
                    inventory.append("fireball")
                    print("the flames go out of control and then completely burn out. A fireball spell is added to your inventory and you continue")
                    lastroom()
                else:
                    print("provide a valid input")
        elif userInput == "equipment":
            equip_stuff()
        elif userInput == "character":
            character_info()
        elif userInput == "info":
            game_info()
        else:
            print("provide a valid input")

def lastroom():
    print("You grab the doorhandle at the other end of the dining hall and hear a voice echo: Well done brave warrior, you have reached the end of this demo adventure. You have completed the adventure with the following stats:")
    character_info()
    quit()

# by this point, the functions aren't called yet so nothing happens :D
# to call it:
EnteringTheDungeon()