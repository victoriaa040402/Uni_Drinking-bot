import time
import random


def timer():
    print("3")
    print("2")
    print("1")
    time.sleep(10)
    print("time's up")
    sip = int(input("How many sips were taken?"))

    return sip


def round1(players, sips):
    deck = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    king = 0
    jack  = ""
    queen = ""
    for i in players:
        print("it's time for", i, "'s turn:")
        print("generating card...")
        print(".")
        print(".")
        print(".")
        card = random.choice(deck)
        print("You got:", card)

        if card == "Ace":
            print(
                "Going around the circle clockwise, each player must starts drinking consecutively and has to continue drinking until the one before has stopped")
            sips += len(deck)

        elif card == "2":
            print("Point to someone to drink")
            sips += 1

        elif card == "3":
            print("You have to drink")
            sips += 1

        elif card == "4":
            print("All the girls must drink")
            sips += 3

        elif card == "5":
            print("Random 2 players must finish their drink before the timelimit ends")
            print(random.choice(players), "and", random.choice(players))
            print("you must both drink until the timelimit ends")
            end = timer()
            sips = sips + end

        elif card == "6":
            print("All the boys must drink")
            sips += 3

        elif card == "7":
            print("The person who drew the card can pick 2 players to finish their drinks before the timelimit")
            time.sleep(3)
            print("timer shall now begin...")
            end = timer()
            sips = sips + end

        elif card == "8":
            print(
                "Choose another player to become your 'mate', this player will have to drink each time you have to during the game")
            time.sleep(1)

        elif card == "9":
            print("""
The computer will generate a random number from 1-10, it is your job to guess it through a series of higher or lower questions, if you guess in under 7 gos,
you chose a player to drink, otherwise, you must drink that number of sips.                
""")
            number = random.randint(1, 10)
            print("I have my number")
            choice = int(input("Guess my number:"))
            counter = 0
            while choice != number and counter < 10:
                if choice < number:
                    print("my number is higher than", choice)
                else:
                    print("my number is lower than", choic)
                counter += 1
                choice = int(input("Guess my number:"))

            if choice == number:
                print("congratulations, you guessed that my number was", choice, "and were correct")
                print("choose a player to drink", number, "sips")
            else:
                print("bad luck, my number was:", number)
                print("you must now take ", number, "sips")
            sips = sips + number

        elif card == "10":
            print("Rock, Paper, Scissors, Winner chooses who drinks")
            RPS = ["rock", "paper", "scissors"]
            print("lets play")
            comp_choice = 0
            choice1 = 0

            while comp_choice == choice1:
                choice1 = input("rock, paper or scissors?")
                comp_choice = random.choice(RPS)
                if choice1 == "rock":
                    if comp_choice == "scissors":
                        print("your victory, pick a player to drink")
                        sips += 1
                    elif comp_choice == "paper":
                        print("my victory, you must take a sip")
                        sips += 1
                    else:
                        print("retry... we drew")
                elif choice1 == "paper":
                    if comp_choice == "rock":
                        print("your victory, pick a player to drink")
                        sips += 1
                    elif comp_choice == "scissors":
                        print("my victory, you must take a sip")
                        sips += 1
                    else:
                        print("retry... we drew")
                elif choice1 == "scissors":
                    if comp_choice == "paper":
                        print("your victory, pick a player to drink")
                        sips += 1
                    elif comp_choice == "rock":
                        print("my victory, you must take a sip")
                        sips += 1
                    else:
                        print("retry... we drew")

        elif card == "Jack":
            if jack  == "":
                print("please enter your own rule")
                jack = input()
            else:
                print(jack)
                sip = int(input("how many sips were taken?"))
                sips = sips + sip

        elif card == "Queen":
            if queen  == "":
                print("please enter your own rule")
                queen = input()
            else:
                print(queen)
                sip = int(input("how many sips were taken?"))
                sips = sips + sip
        time.sleep(4)

    else:
        king += 1
        if king ==  4:
            print("unlucky, you are the 4th king!")
            print("you must now drink: ", sips, "sips, or face a forfeit decided by the group")
            print("sips are now wiped")
            sips = 0
            king = 0
        else:
            print("you are the ", king, " king")
        return sips


def rounds(players, sips):
    count = 1
    card = ""
    jack = ""
    queen = ""
    king = 0
    sips = 0

    while count <= 10:
        print("round ", count)
        sips = round1(players, sips)
        count += 1


def ringOfFire(players):
    ready = 0
    sips = 0
    print("""
welcome to ring of fire.
*loading game...*
""")
    time.sleep(1.5)
    print("""
the rules are as followed:
one by one each player will be  given one of the following cards at random - it is there responsibilty
to perform the task that will be suggested
""")
    while ready != "yes":
        print("are  you ready?")
        ready = input("type 'go back' if not and yes otherwise:")
        time.sleep(1)
    print("""
the card deck and respective  rules:
- Ace: Going around the circle clockwise, each player starts drinking consecutively and has to continue drinking until the one before has stopped
- Two: Point to someone to drink
- Three: You have to drink
- Four: All the girls must drink
- Five: Random 2 players must finish their drink before the timelimit ends
- Six: All boys must drink
- Seven: The person who drew the card can pick 2 players to finish their drinks before the timelimit
- Eight: Choose another player to become your 'mate', this player will have to drink each time you have to during the game
- Nine: The computer will generate a random number, it is your job to guess it through a series of higher or lower questions, if you guess in under 10, you
        chose a player to drink, otherwise, you must drink that number of sips.
- Ten: Rock, Paper, Scissors, Winner chooses who drinks
- Jack: Come up with a rule for this card
- Queen: Come up with a rule for this card
- King: Skip around until the 4th is played, the 4th time, the player must take as many sips as have happened throughout the entire game
""")
    time.sleep(3)
    print("Beginning the game....")
    rounds(players, sips)
