game = "Exploration Sim"
print("Hi! Welcome to", game + ". What's your name?")
reqAge = 18
health = 3
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
    ans = input("That works for me! Do you actually want to play though?(Y/N) ")
    ans = ans.lower()
    if ans == "y":
        print("Cool, let's go! Your starting health is 3.")
    else:
        exit()
elif int(age) == reqAge - 1:
    print(f"LMAO almost there little buddy, wait until you turn {reqAge} years old")
else:
    print("Oof... You will have to wait", reqAge - int(age), "year(s) before you can play.")
prompt1 = "You walk out of your house. In front of you is an unlocked bike (1), to your left is a brand new MG3 (2). Which do you take? "
choice1 = input(prompt1)
if choice1 == "1" or "bike":
    print("You get on the bike and start riding, as you realise you never learned and promptly fall off. you lose one life.")
    health -= 1
    print(f"You have {health} health left")
elif choice1 == "2" or "MG3":
    choice1b = input("You feel around in your pockets, but there is no key. Do you want to try to jack the car (1), go back inside to search for the keys (2) or take the bike anyway (3)?")
    if choice1b == "1" or "jack":
        print("An alarm goes off. you run away and lose one health from the shock.")
        health -= 1
        print(f"You have {health} health left")
    elif choice1b == "2" or "go back":
        choice1bb = input("You left the door locked. Climb through the window (1) or walk around the back (2)? ")
        if choice1bb == "1" or "climb":
            print("You're in!")
        elif choice1bb == "2" or "walk around":
            print("Damn, this door is also locked. Lose 1 health out of embarrassment")
            health -= 1
            print(f"You have {health} health left")
    elif choice1b == "3" or "take bike":
        print("You get on the bike and start riding, as you realise you never learned and promptly fall off. you lose one health.")
        health -= 1
        print(f"You have {health} health left")
