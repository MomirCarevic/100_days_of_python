import random

words_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Create a placeholder with the same number of blanks as chosen word

chosen_word = random.choice(words_list)
print(chosen_word)

numberOfLetters = len(chosen_word)

for n in range(0,numberOfLetters) :
    print("_",end="")

# TODO-2 - Create a "display" that puts the guess letters in the right place

guess = input("\nGuess a letter: ")

for n in range(0,numberOfLetters) : 
    if guess.lower() == chosen_word[n] :
        print(f"{guess.lower()}",end="")
    else : 
        print("_",end="")
