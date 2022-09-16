


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
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;   =           |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("Pls you will be asked some question so write with your first word in capital letter.")
print("Welcome to the Treasure Island")
print("Your mission is to find the missing treasure")
choice1=input("You are at the crossroads wher will you follow 'Left' or 'Right'.")
if choice1 !='Right':
   print("You followed the wrong way Game.over.")
   exit()

   


   
choice2=input("You have reached the lake type 'Swim' to swim across-the-board or type 'Wait' to wait for ⛴ boat.")
if choice2!='Wait' :
   print("You dronwed into the water full of crocodiles Game.over.")
   exit()
else:
   print("Good going.")

   
choice3=input("The boat led you to 3 doors,which one are you going to enter. type 'Red', 'Blue' or 'Yellow'")
if choice3!='Blue':
   print ("You entered the house 🏘 of monsters.GAME.OVER.")
else:   
   print("You Win. Thanks for playing python game.") 
