import random

words_list = ["aardvark", "baboon", "camel"]
ctr = 0
win = False
correctLetter = []


chosen_word = random.choice(words_list)
print(chosen_word)

numberOfLetters = len(chosen_word)

while not win :
    guess = input("\nGuess a letter: ").lower()
    
    display = ""

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
    
    if ctr == numberOfLetters :
        win = True
    else :
        win = False

