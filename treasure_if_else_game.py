print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
fork = input("You have been walking for hours and stumble along a fork in the road. Do you go left or right?")
if fork == "Right" or fork == "right":
    bridge = input(
        "You turn right and come to a bridge. Do you cross the bridge or stop and get some water? Enter cross or water")
    if bridge == "Cross" or bridge == "cross":
        treasure = input("After crossing the bridge you find your way into the middle of the island and come across a "
                         "cave. Do you enter the cave or continue on? Enter Yes to go into the cave. Enter No to continue on.")
        if treasure == "Yes" or treasure == "yes":
            print("You slowly peek inside the cave and see a shiny crate. You found the treasure congratulations!")
        else: print("You continue on the path and are attacked by island inhabitants. Game Over!")
    else:
        print("You lean down to the waters edge to get a drink and are quickly attacked by a crocodile. Game Over!")

else: print("You begin left down the trail and fall into a booby trap to your death. Game Over!")


