import art
import random
from game_data import data
score = 0
guess = True

while guess == True :
    print(art.logo)
    print(random.choice(game_data.data))

    Continue = input("Do you want to continue? 'yes' or 'no'")

    if Continue == 'yes' :
        guess = True 
    elif Continue == 'no' :
        guess = False


