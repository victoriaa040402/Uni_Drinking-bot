import random
import webbrowser
def alphabetGame(playerNum):
    print("The Rules of the game are simple:\n 1. You will be tasked with inputting a word which begins with a random letter and is between 3-6 letters long. \n 2. You will have to decide as a group a time limit and enforce it yourselves.\n 3. If you fail, you drink.")
    rounds= 1
    while rounds <6:
        for i in range(0, playerNum):
            x = playing(i)
            if x == True: 
                print("You have passed round " +str(rounds) + ", onto the next person")
            elif x == False:
                print("You have failed round "+ str(rounds) +" and must drink")
            i+=1
        rounds += 1
    print("The game is now over, whoever is the least drunk wins")

def playing(player):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    wordLength = random.randint(3,6)
    wordStart = random.choice(alphabet)
    answer = input("Player "+ str(player+1)+ " enter a "+ str(wordLength) + " letter word beginning with "+ wordStart+".")
    answer.lower()
    if wordStart == answer[0] and len(answer) == wordLength:
        return True
    else:
        return False
