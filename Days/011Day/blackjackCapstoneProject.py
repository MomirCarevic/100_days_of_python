import random
from os import system
from art import logo

def checkCards(card) :
    if sum(card.values()) > 21 :
        for key in card :
            if card[key] == 11 :
                card[key] = 1
    
    print(card)
    return int(sum(card.values()))

def checkWinner(sum1,sum2) :
    if sum1 > 21 :
        result = False
    elif sum2 > 21 and sum1 < 22 :
        result = True
    elif sum1 > sum2 :
        result = True
    elif sum1 == sum2 :
        result = "Draw"
    else :
        result = False
    print(f"player result {sum1} | dealer result {sum2} | {result}")
    

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
result = True

player_card = {}
dealer_card = {}

start_game = input("Do you want to play a game of Blackjack? Type 'yes' or 'no'\n")

while start_game == 'yes' :
    system("cls")
    print(logo)
    
    player_card[1] = random.choice(cards)
    player_card[2] = random.choice(cards)
    
    dealer_card[1] = random.choice(cards)
    dealer_card[2] = random.choice(cards)



    print(f"Player cards are [{player_card[1]}|{player_card[2]}]")
    print(f"Dealer cards are [{dealer_card[1]}|##]")

    choice = input("Do you want to pull another card?\n Type 'hit' or 'stand'\n")

    if choice == 'stand' :
        #check player cards
        player_sum = checkCards(card=player_card)
        dealer_sum = checkCards(card=dealer_card)
        checkWinner(sum1=player_sum,sum2=dealer_sum)


    elif choice == 'hit' :
        player_card[3] = random.choice(cards)
        player_sum = checkCards(card=player_card)
        dealer_sum = checkCards(card=dealer_card)

        if dealer_sum < 16 :
            n = 3
            while dealer_sum <16 :
                dealer_card[n] = random.choice(cards)
                dealer_sum = checkCards(card=dealer_card)
                n += 1

        checkWinner(sum1=int(player_sum),sum2=int(dealer_sum))
            

    start_game = input("Do you want to play again? Type 'yes' or 'no'\n")

    #   RESETING VARIABLES #
    player_card = {}
    dealer_card = {}
    n = 3
    
