from os import system
import art
import random
from game_data import data

ctr = 0
score = 0
guess = True

def loadData(new_data) :
    new_data = random.choice(data)
    return new_data

def printData(dict) :
    print(f" {dict.get("name")}", end="")
    if dict.get("description") != "None" :
        print(f", a {dict.get("description")}",end="")
    if dict.get("country") != "None" :
        print(f", from {dict.get("country")}")
    
    #This print is only for testing purposes
    #print(f"{dict.get("follower_count")}")

def printQuestion(dict1,dict2) :
    print("Compare A: ",end="") 
    printData(dict=A)
    print(art.vs)
    print("Against B: ",end="") 
    printData(dict=B)

def checkResult(answer, dict1, dict2) :
    global ctr
    global guess

    if A.get("follower_count") > B.get("follower_count") :
        if answer == 'A' :
            ctr += 1
        else :
            guess = False
    elif B.get("follower_count") > A.get("follower_count") :
        if answer == 'B' :
            ctr += 1
        else :
            guess = False

#   Setting up the game        

A = {}
B = {}

print(art.logo)
A = loadData(A)

while guess == True :
    
    B = loadData(B)
    
    printQuestion(dict1=A,dict2=B)

    choseAnswer = input("Who has more followers? Type 'A' or 'B'\n")
    checkResult(answer=choseAnswer,dict1=A,dict2=B)

    if guess == False :
        break
    
    #   Setting up next question 

    system("cls")
    print(art.logo)
    print(f"You're right! Current score: {ctr}")

    A = B

print(f"Sorry, that's wrong. Final score: {ctr}")

