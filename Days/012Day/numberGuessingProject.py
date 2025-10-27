#   Hard level - 5 attempts
#   Easy level - 10 attempts

import random



def checkNumber(guess,number) :
    if guess > number :
        print("Too high.")
    elif guess == number :
        return True
    else : 
        print("Too low.")
    return False

print("Welcom to Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': \n")

nummber = random.randint(1,100)

if difficulty == 'easy' :
    attempts = 10
elif difficulty == 'hard' :
    attempts = 5
print(nummber)

while attempts > 0 :
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    win = checkNumber(guess=guess,number=nummber)
    if win == True :
        print("You guess correctly!")
        break
    else :
        attempts -= 1

if win == False :
        print("You've run out of guesses, you lose!")
    
