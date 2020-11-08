print("Welcome! I am the bot for drinking games.")
print("Due to COVID-19 restrictions you can only have a maximum of 6 players")
list=[]
n=int(input("Enter number of players:"))
for i in range(0,n):
    name=str(input("Enter you name:"))
    list.append(name)
print("Welcome: " + ', '.join(list))
print("1.Jacks Drinking Game")
print("2.Anna's Drinking Game")
game=input("What game would you like to play: ")
