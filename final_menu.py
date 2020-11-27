print("Welcome! I am the bot for drinking games.\n"
      "Here you will have the choice to play two drinking games while having the\n"
      "opportunity to listen to some music.")
print("Due to COVID-19 restrictions you can only have a maximum of 6 players")
players=[]
n=int(input("Enter number of players: "))
for i in range(0, n):
    name = str(input("Enter you name: "))
    players.append(name)
print("Welcome: " + ', '.join(players))
from game1 import *
count = 0
def menuOptions():
    game = input("What game would you like to play:\n"
                 "1. Alphabet Game \n"
                 "2. Ring O Fire\n"
                 "3. Listen to music (this is not a game)\n"
                 "4. Cocktail Tracing and Making\n"
                 " ")
    return game

from drinks import *
from game2 import *
while count == 0:
     game = menuOptions()
     if game == "1":
        alphabetGame(len(players))
     elif game == "3":
         import webbrowser
         link = input("Enter a youtube link for the song you wish to hear. "
                    "Or select a playlist: \n"
                    "1. Rock Playlist\n"
                    "2. Pop Playlist\n"
                    "3. Hip Hop Playlist\n"
                    "4. Classical Music Playlist\n"
                    "To return to game enter 0.\n")
         if link =="0":
             count=0
         elif link =="1":
             webbrowser.open("https://www.youtube.com/watch?v=ktvTqknDobU&list=PLzxEw1CbicllxqVJaN9hodbkMXNX0Cnds")
         elif link == "2":
             webbrowser.open("https://www.youtube.com/watch?v=SlPhMPnQ58k&list=PL4o29bINVT4EG_y-k5jGoOu3-Am8Nvi10")
         elif link == "3":
             webbrowser.open("https://www.youtube.com/watch?v=JFm7YDVlqnI&list=PL-FVH5VWgRPHNz24zZ5_FLHQWoidN6O1d")
         elif link == "4":
             webbrowser.open("https://www.youtube.com/watch?v=K1SQh0JI5JQ&list=PL1mZeR4wTBoyFZMFCUsPqpgGO2tPd4eAe")
         else:
             webbrowser.open(link)
     elif game == "2":
         ringOfFire(players)
     elif game == "4":
         drinkChoice=input("Would you like a Premade drink or Make Your Own?").lower()
         if drinkChoice == "1" or "premade":
             premade()
         elif drinkChoice == "2" or "make your own":
             ownCocktail()
     else:
        count = 0
