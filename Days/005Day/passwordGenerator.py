# DAILY PROJECT     :       PASSWORD GENERATOR

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

letters_new = []
symbols_new = []
numbers_new = []
password = []

print("Welcome to the PyPassword Generator!\n")
letters_number = int(input("How many letters would you like in your password!\n"))
symbol_number = int(input("How many symbols would you like?\n"))
number_number = int(input("How many numbers would you like?\n"))

for number in range(0,letters_number) :
    lettersSeed = random.randint(0,len(letters))
    letters_new.append(letters[lettersSeed-1])

for number in range(0,number_number) :
    numbers_new.append(random.choice(numbers))

for number in range(0,symbol_number) :
    symbolSeed = random.randint(0,len(symbols))
    symbols_new.append(symbols[symbolSeed-1])

password = letters_new + numbers_new + symbols_new
random.shuffle(password)

final_password ="".join(password)

print(f"Your password is {final_password}")