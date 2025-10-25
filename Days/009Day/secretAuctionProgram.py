from os import system

bidders = {}

other_bidders = 'yes'

print("Welcome to the secret auction program.")

while other_bidders == 'yes' :
    name = input("What is your name? ")
    bid = int(input("What is your bid? "))
    bidders[name] = bid

    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")



    if other_bidders == 'yes' :
        system("cls")
    elif other_bidders == "no" :
        print("Bidding has ended\n")

winning_bidder = max(bidders, key=bidders.get)
max_bid = bidders[winning_bidder]

print(f"Max bid is {max_bid} set by {winning_bidder}\n")