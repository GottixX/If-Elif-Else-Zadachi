from random import randint 


sides = input("Enter Dice Sides: ")
name1 = input("Player1 name? : ")
name2 = input("Player2 name? : ")
sides = int(sides)
roll1 = randint(1,sides)
roll2 = randint(1,sides)
input (name1 + " rolls " + str(roll1))
input (name2 + " rolls " + str(roll2))
if roll1 > roll2:
    print (name1 + " wins the game!!")
elif roll1 < roll2:
    print (name2 + " wins the game ")
else:
    print ("It's a draw")
