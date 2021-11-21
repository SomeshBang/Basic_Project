# Dice genrator
# Head or Tails

import random
import time

while True:
    print("1.Dice Genrator")
    print("2.Head Or Tails")
    print("3.Try both ... ??")
    print("4.Exit")
    print("-------------------------")
    x=input("Enter Your Choice....")
    print("-------------------------")

    # Dice genrator
    if int(x) == 1:   
        print("Dice is Rolling....")
        time.sleep(3)
        dice = [1, 2, 3, 4, 5, 6]
        print("Answer is = ",random.choice(dice))
        print("-------------------------")
        print("    ")

    # Head or Tails
    elif int(x) == 2:
        h_t=["Head","Tails"]
        print("Coin is Fliping....")
        time.sleep(3)
        print("Flipped Coin is ",random.choice(h_t))
        print("-------------------------")
        print("    ")

    # Both
    elif int(x) == 3:
        print("Dice is Rolling....")
        time.sleep(3)
        dice = [1, 2, 3, 4, 5, 6]
        print("Answer is = ",random.choice(dice))
        print(" ")
        h_t=["Head","Tails"]
        print("Coin is fliping....")
        time.sleep(3)
        print("Flipped Coin is ",random.choice(h_t))
        print("-------------------------")
    
    else:
        break
