import random
from hangman_words import word_list
from hangman_art import stages
from hangman_art import logo

ctr = 0
win = False
lose = False
lives = 6
correctLetter = []

chosen_word = random.choice(word_list)
print(logo)
print(chosen_word)

numberOfLetters = len(chosen_word)

while not win :
    print(f"Number of lives: {lives}")
    guess = input("\nGuess a letter: ").lower()
    
    display = ""

    ctr_old = ctr

    for letter in chosen_word : 
        if guess == letter :
            display += guess
            correctLetter.append(guess)
            ctr += 1
        
        elif letter in correctLetter:
            display += letter

        else : 
            display += "_"
    
    print(display)
    print(stages[lives-1])

    if guess not in chosen_word :
        lives -= 1
        
        if lives == 0 :
            win = True
            print("YOU LOSE!\n")

    if ctr == numberOfLetters :
        win = True
        print("YOU WIN!\n")
    
    

