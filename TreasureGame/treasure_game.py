#Topics: #MultilineStrings #If-elif-else #StringLowerMethod #ConditionalOperator

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
print("Welcome to Star's Treasure Island!")
print("Your mission is to find the lost treasure.") 

print("You are at a cross road. Where do you want to go? Type 'left'/'right'/'forward'/'backward'.\nRemember only one road leads to the treasure.")
direction = input().lower()

if direction == "left":  
  print("You are smart!")
  print("You have travelled 5km, but you path is blocked by a river.\nYou can either swim across or wait for boat to arrive")
  
  print("What do you choose? Type 'wait' or 'swim'")
  choice = input().lower()
  
  if choice == "wait":
    print("Your boat has arrived! Hop on.")
    print("Finally you have reached the castle where your treasure is hidden.")
    print("You see 5 doors with different colors: Red, Blue, Green, Yellow, Black.")
    
    print("Which door do you choose? Type 'red'/'blue'/'green'/'yellow'/'black'.")
    door_color = input().lower()
    
    if door_color == "yellow":
      print("You found the treasure! You have won the game!")
    elif door_color == "red" or door_color == "green":
      print(f"You have been eaten by a {door_color} monster. Game Over.")
    elif door_color == "blue":
      print("Oh! This a portal to center of the ocean. You drowned! Game Over.")
    else:
      print("You got sucked in to a dark hole! Game Over.")
  else:
    print("The river monster noticed you! Game Over.")
else:
  print("I warned you...\nYou chose the wrong direction and got lost in the maze! Game Over.")
