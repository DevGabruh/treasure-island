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

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

path = input("1. Will you take the left or right path?\n").casefold()
if path == "left":
  print("~As you walk down the path on the left you notice a beast the size of a bear stalking you and decide to run as fast as you can. As you run for your life you notice a river.~\n")
  swim = input(" [swim] or [fight]?\n").lower()
else:
  print("As you walk down the path to the right you notice the bushes to your right shaking then suddenly an arrow hits you between the brows and you drop to the ground dead. Game Over.")

swimming = swim
if swimming == "swim":
  print("~You swim across with all your might and when you make it to the other side you only see 3 different color doors in front of you. A red, blue and yellow door. Which one will you choose?")
  door = input("r / b / y:\n ").casefold()
  if door == "r":
    print("You enter the red and door and the door instantly shuts closed on its own. You burn to a crisp. Game over.")
  elif door == "b":
    print("You enter the blue door and then suddenly the door closes on you. Water comes from all sides and you drown. Game Over.")
  if door == "y":
    print("You enter the yellow door and a warm light kisses your forehead. All you see around you is gold. You win.")
else:
  print("You tried to fight a bear like beast and the beast ripped you to shreds. You're dead. Game over.")