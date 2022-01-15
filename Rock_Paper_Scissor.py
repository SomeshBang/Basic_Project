import random
import time
z = True

while z:
    time.sleep(2)
    print("Choose your option ")
    print("1.Rock \n2.Paper \n3.Scissor \n4.Exit Game")
    ply1 = input("Enter your Choice - ")
    print("---------------------------------------------")
    try:
        if int(ply1) == 1 or 2 or 3:
            compu = [1,2,3]
            ply2 = random.choice(compu)

            if int(ply1) == int(ply2):
                if int(ply1) == 1:
                    print("You have selected Rock \nPlayer 2 has selected Rock \n\nIt is Tie....!!")
                elif int(ply2) == 2:
                    print("You have selected Paper \nPlayer 2 has selected Paper \n\nIt is Tie....!!")
                else:
                    print("You have selected Scissor \nPlayer 2 has selected Scissor \n\nIt is Tie....!!")

            elif int(ply1) == 1 and int(ply2) == 2 :
                print("You have selected Rock \nPlayer 2 has selected Paper \n\nPlayer 2 has Won....!!")
            elif int(ply1) == 1 and int(ply2) == 3:
                print("You have selected Rock \nPlayer 2 has selected Scissor \n\nYou Won....!!")

            elif int(ply1) == 2 and int(ply2) == 1:
                print("You have selected Paper \nPlayer 2 has selected Rock \n\nYou Won....!!")
            elif int(ply1) == 2 and int(ply2) == 3:
                print("You have selected Paper \nPlayer 2 has selected Scissor \n\nPlayer 2 Won....!!")

            elif int(ply1) == 3 and int(ply2) == 1:
                print("You have selected Scissor \nPlayer 2 has selected Rock \n\nPlayer 2 Won....!!")
            elif int(ply1) == 3 and int(ply2) == 2:
                print("You have selected Scissor \nPlayer 2 has selected Paper \n\n\nYou Won....!!")
            print("-------------------------------------------------")

        if int(ply1) == 4:
            z = False
        elif int(ply1) >=5:
            print("Enter Valid Input")
            print("-------------------------------------------------")

    except Exception as e:
        pass
