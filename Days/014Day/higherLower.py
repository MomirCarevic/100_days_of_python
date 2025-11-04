import art
import random
from game_data import data
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

def printQuestion(dict1,dict2) :
    print("Compare A: ",end="") 
    printData(dict=A)
    print(art.vs)
    print("Against A: ",end="") 
    printData(dict=B)

A = {}
B = {}

while guess == True :
    print(art.logo)

    A = loadData(A)
    B = loadData(B)
    
    printQuestion(dict1=A,dict2=B)


    Continue = input("Do you want to continue? 'yes' or 'no'")

    if Continue == 'yes' :
        guess = True 
    elif Continue == 'no' :
        guess = False


