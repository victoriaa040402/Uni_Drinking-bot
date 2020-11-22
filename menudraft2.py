print("Welcome! I am the bot for drinking games.")
print("Due to COVID-19 restrictions you can only have a maximum of 6 players")
list=[]
n=int(input("Enter number of players:"))
for i in range(0,n):
    name=str(input("Enter you name: "))
    list.append(name)
print("Welcome: " + ', '.join(list))
from game1 import *
count = 0
game = input("What game would you like to play:\n"
                 "1. Alpabet Game \n"
                 "2. Anna's Game \n"
                 "3. Listen to music (this is not a game)\n"
                 " ")
while count == 0:
     if game == "1":
        alphabetGame(len(list))
        count+=1
     elif game=="3":
         import webbrowser
         link=input("Enter a youtube link for the song you wish to hear. \nTo return to game enter 0.\n")
         if link == "0":
             count = 0
             game = input("What game would you like to play:\n"
                          "1. Alpabet Game \n"
                          "2. Anna's Game \n"
                          "3. Listen to music (this is not a game)\n"
                          " ")
         else:
             webbrowser.open(link)
     else:
        count = 0
        game = input("What game would you like to play:\n"
                     "1. Alpabet Game \n"
                     "2. Anna's Game \n"
                     "3. Listen to music (this is not a game)\n"
                     " ")
