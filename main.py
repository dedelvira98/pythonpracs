import random
min = 1
max = 6

def roll():
    roll_again = "yes"
    while roll_again == "yes":
        print ("Roll the dice...")
        print ("The Values are")
        print (random.randint(min, max))
        roll_again = "no"

roll()
again = input("Do you still want to throw the dice?")

if again == "yes":
    roll()
else:
    print("Thank You, See You Again!")

again = input("Do you still want to throw the dice?")

if again == "yes":
    roll()
else:
    print("Thank You, See You Again!")