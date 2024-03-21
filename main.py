game = "Exploration Sim"
print("Hi! Welcome to", game + ". What's your name?")
reqAge = 18
health = 3


def check_health():
    if health < 1:
        print("You dead")
        exit("rip in pieces")
    else:
        print(f"{health} health points left...")


name = input()
validAge = False
while not validAge:
    age = input("...and how old are you? ")
    if age.isdigit():
        validInt = True
        break
    else:
        print('The input is not a valid number. Please restart the game.')
        exit()
if int(age) >= reqAge:
    wants_to_play = input("That works for me! Do you actually want to play though?(Y/N) ").lower()
    if wants_to_play == "y" or wants_to_play == "yes":
        print("Cool, let's go! Your starting health is 3.")
    else:
        print("Well why did you start the game then...")
        exit()
elif int(age) == reqAge - 1:
    print(f"LMAO almost there little buddy, wait until you turn {reqAge} years old")
else:
    print("Oof... You will have to wait", reqAge - int(age), "year(s) before you can play.")
    exit("Byeeeee")
choice1 = input("You walk out of your house. In front of you is an unlocked bike (1), to your left is a brand new MG3 (2). Which do you take? "
)
if choice1 == "1" or choice1 == "bike":
    print("You get on the bike and start riding, as you realise you never learned and promptly fall off. you lose one life.")
    health -= 1
    check_health()
    choice1_1 = input("Do you want to try again?(Y/N) ").lower()
    if choice1_1 == "y":
        print("Hey, you're starting to get this! Look at you g.. okay you should steer now... left or right, it doesn't mat... *BLAM!*")
        health -= 1
        print("Yeah you have a concussion for sure now... You're also bleeding! Better go get some help.")
        check_health()
        choice1_1_1 = input("Get help or bleed out (1/2)? ").lower()
        if choice1_1_1 == "1" or choice1_1_1 == "get help":
            print("You crawled back to your house and managed to dial 911 before passing out. They came to pick you up and you woke up in the hospital a day later, feeling like you headbutted a wrecking ball.")
            health += 1
            check_health()
        else:
            print("Well I guess you're done with whatever this was...")
            health -= 1
            check_health()
elif choice1 == "2" or choice1 == "MG3":
    choice1b = input("You feel around in your pockets, but there is no key. Do you want to try to jack the car (1), go back inside to search for the keys (2) or take the bike anyway (3)?")
    if choice1b == "1" or choice1b == "jack":
        print("An alarm goes off. you run away and lose one health from the shock.")
        health -= 1
        check_health()
    elif choice1b == "2" or choice1b == "go back":
        choice1bb = input("You left the door locked. Climb through the window (1) or walk around the back (2)? ")
        if choice1bb == "1" or choice1bb == "climb":
            print("You're in!")
        elif choice1bb == "2" or choice1bb == "walk around":
            print("Damn, this door is also locked. Lose 1 health out of embarrassment")
            health -= 1
            check_health()
    elif choice1b == "3" or choice1b == "take bike":
        print("You get on the bike and start riding, as you realise you never learned and promptly fall off. you lose one health.")
        health -= 1
        check_health()

game_end = f"Congratulations! You completed the game with {health} health points remaining!"
print(game_end)