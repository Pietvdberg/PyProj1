game = "Exploration Sim"
print("Hi! Welcome to", game + ". What's your name?")
reqAge = 18
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
    print("That works for me! Good luck", name + "!")
else:
    print("Oof... You will have to wait", reqAge - int(age), "year(s) before you can play.")
