from os import system
from art import logo

start_game = input("Do you want to play a game of Blackjack? Type 'yes' or 'no'\n")

while start_game == 'yes' :
    system("cls")
    print(logo)
    #start_game = 'no'