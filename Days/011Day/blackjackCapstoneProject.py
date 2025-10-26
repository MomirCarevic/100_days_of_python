import random
from os import system
from art import logo

#def checkCards(card1,card2,card3) :
    

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
result = True

start_game = input("Do you want to play a game of Blackjack? Type 'yes' or 'no'\n")

while start_game == 'yes' :
    system("cls")
    print(logo)
    
    player_card1 = random.choice(cards)
    player_card2 = random.choice(cards)
    
    dealer_card1 = random.choice(cards)
    dealer_card2 = random.choice(cards)



    print(f"Player cards are [{player_card1}|{player_card2}]")
    print(f"Dealer cards are [{dealer_card1}|##]")

    choice = input("Do you want to pull another card?\n Type 'hit' or 'stand'\n")

    if choice == 'stand' :
        #check player cards
        playerSum = player_card1+player_card2
        dealerSum = dealer_card1 + dealer_card2

        if playerSum > 21 :
            result = False
        elif dealerSum > 21 and playerSum < 22 :
            result = True
        elif playerSum > dealerSum :
            result = True
        elif playerSum == dealerSum :
            result = "Draw"
        else :
            result = False
        print(f"player result {playerSum} | dealer result {dealerSum} | {result}")
        # check dealer cards  

    start_game = input("Do you want to play again? Type 'yes' or 'no'\n")