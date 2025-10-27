# Target is the number up to which we count
def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0:
            if number % 5 == 0:
                print("FizzBuzz")
            else : 
                print("Fizz")
            
        elif number % 5 == 0:
            print("Buzz")
        else:
            print([number])

fizz_buzz(15)