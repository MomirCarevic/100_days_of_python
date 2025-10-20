import random

#   adding Rock, Paper, Scissors ASCII art

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

hand_sign = [rock, paper, scissors]

player_1 = hand_sign[random.randint(0,2)]
player_2 = hand_sign[random.randint(0,2)]

print(player_1)
print(player_2)

if player_1 == rock :
    if player_2 == paper :
        print("PLAYER 2 WINS!")
    elif player_2 == scissors :
        print("PLAYER 1 WINS!")
    else :
        print("TIE")
elif player_1 == paper :
    if player_2 == scissors :
        print("PLAYER 2 WINS!")
    elif player_2 == rock :
        print("PLAYER 1 WINS!")
    else :
        print("TIE")

elif player_1 == scissors :
    if player_2 == rock :
        print("PLAYER 2 WINS!")
    elif player_2 == paper :
        print("PLAYER 1 WINS!")
    else :
        print("TIE")
