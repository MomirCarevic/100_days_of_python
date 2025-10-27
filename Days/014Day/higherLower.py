import art
import random
from game_data import data
score = 0
guess = True

def loadData(dictionary,random) :
    #loading data into a dictionary
    dictionary = {**data[random]}

A = {}
B = {}

while guess == True :
    print(art.logo)
    
    print(random.choice(data))
    loadData(dictionary=A,random=random.choice(data))
    Continue = input("Do you want to continue? 'yes' or 'no'")

    if Continue == 'yes' :
        guess = True 
    elif Continue == 'no' :
        guess = False


