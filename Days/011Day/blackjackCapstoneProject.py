import random
from os import system
from art import logo

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

start_game = input("Do you want to play a game of Blackjack? Type 'yes' or 'no'\n")

while start_game == 'yes' :
    system("cls")
    print(logo)
    
    card1 = random.choice(cards)
    card2 = random.choice(cards)
    
    print(card1,card2)

    start_game = 'no'