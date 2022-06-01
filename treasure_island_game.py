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
print("Your mission is to find the treasure (and who knows what else, wink wink).")

choice1 = input('You\'re at a cross road with no signs. Where do you want to go? Type "left", "right" or straight ahead \n').lower()
if choice1 == "left":
  choice2 = input('You\'ve come to a glowing lake. There is an misty island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
  if choice2 == "wait":
    choice3 = input("You arrive at the island unharmed, but naked? hu. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
    if choice3 == "red":
      print("You find a book that's cursed, you can't stop reading the book and it never ends. Game Over.")
    elif choice3 == "yellow":
      print("You found the treasure! But also a powerul spellbook! Your now an apprentice witch and more adventures awaite. You Win!")
    elif choice3 == "blue":
      print("You enter a room of passionet young wearwolfs. I'll leave the rest to your imagination, wink wink. Game Over.")
    else:
      print("You chose a door that doesn't exist. Your now under a strange spell and stuck here forever....and naked. Game Over.")
  else:
    print("You meet a lonely merman who seduces you. You are now a merman and live in the lake with him. Game Over.")
elif choice1 == "right":
    print("You fell into a hole and met a beautiful drow prince. You fell in love and live in his underground kingdom for at least 1000 years. Game Over.")
else:
    print("you met a cute satyr, fell in love and stayed in his forest world forever! You are now magical and can frolic around all day and night!")


