import random as r  # used to pick a random string from a list
import time  # used to have breaks between consecutive print statements

def premade():
    print("Welcome to the premade cocktails menu!")
    time.sleep(1)
    print("This is where we choose your cocktails!")
    premadeCocktails = ["Blue Lagoon", "Long Island Ice Tea", "Mojito", "Ginberry fizz", "Aperol Spritz"]
    print(premadeCocktails)
    yourChoice = []
    numOfCocktails = int(input('How may cocktails do you want?'))

    try:
        for i in range(0, numOfCocktails):
            yourChoice.append(premadeCocktails[r.randint(0, len(premadeCocktails))])

    except IndexError:
        print("Sorry, you've taken all the drinks we have!")

    print("Your Drinks Are:")
    print(yourChoice)


def ownCocktail():
    print("Welcome to the make your own cocktail!")
    time.sleep(1)
    chosenSpirit = input("Firstly, please choose a spirit, we currently have Vodka, Rum, Gin or Whiskey ").lower()

    if chosenSpirit == ("vodka"):
        print("Success, spirit has been chosen!")

    elif chosenSpirit == ("rum"):
        print("Success, spirit has been chosen!")

    elif chosenSpirit == ("gin"):
        print("Success, spirit has been chosen!")

    elif chosenSpirit == ("whiskey"):
        print("Success, spirit has been chosen!")
    else:
        print("Please enter a valid spirit")
        ownCocktail()

    chosenMixer = input("Please choose a mixer out of Coke, Lemonade, Orange Juice").lower()

    if chosenMixer == ("coke"):
        print("Added to spirit of choice")

    elif chosenMixer == ("lemonade"):
        print("Added to spirit of choice")

    elif chosenMixer == ("orange juice"):
        print("Added to spirit of choice")
    else:
        print("Please try again")
        ownCocktail()

    print("Your drink is:")
    print(chosenSpirit, "and", chosenMixer)
