from os import system
from calculator_art import art

def add(number1,number2) :
    return number1 + number2

def subtract(number1,number2) :
    return number1 - number2

def multiply(number1,number2) :
    return number1 * number2

def divide(number1,number2) :
    return number1 / number2

print(art)
while 1 :
    continuation = 'y'
    number1 = int(input("What's your first number? "))

    while continuation == 'y' :
        operatio = input("+\n-\n*\n/\nPick your operation:\n")
        number2 = int(input("What's the next number? "))

        if operatio == '+' :
            result = add(number1=number1,number2=number2)
        elif operatio == '-' :
            result = subtract(number1=number1,number2=number2)
        elif operatio == '*' :
            result = multiply(number1=number1,number2=number2)
        elif operatio == '/' :
            result = divide(number1=number1,number2=number2)

        print(f"{number1} {operatio} {number2} = {result}")
        continuation = input(f"Type 'y' to continue calculating with {result} or type  'n' to start new calculation: ")

        if continuation == 'y' :
            number1 = result
        if continuation == 'n' :
            system("cls")
