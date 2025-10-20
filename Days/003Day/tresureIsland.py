'''
Todays final project is to make Tresure Island game.
Date: 20/10/2025

'''
print(r"""
                              .--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
               '-._'-.|| |' `_.-'
                    '-.||_/.-' 
""")

which_way = input("Welcome to Treasure Island. Your mission is to find the treasure.\nYou are at a crossroad, wher do you go left or right?\n")

if which_way == "Left" or which_way == "left" :
    swim_wait = input("Do you swim or wait\n")
    if swim_wait == "Wait" or swim_wait == "wait" :
        which_door = input("Which door color do you chose? Red, Blue or Yellow?\n")
        if which_door == "Red" :
            print("You were eaten by beast, GAME OVER!")
        elif which_door == "Blue" :
            print("You were burnt by fire, GAME OVER!")
        elif which_door == "Yellow" :
            print("YOU WIN!\n")
        else :
            print("GAME OVER!\n")
    else:  
        print("You were attacked by trout, GAME OVER!\n")
else :
    print("You fell into a hole, GAME OVER!\n")
