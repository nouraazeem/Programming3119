"""1. Write a Python program that prompts the user to enter the current month name and prints the season for that month. """

month= input("What month is it?")
if month in ['December', 'January', 'February']:
	winter= "The season is Winter"
	print(winter)

elif month in ['March', 'April', 'May']:
	spring= "The season is Spring"
	print(spring)

elif month in ['June', 'July', 'August']:
	summer= "The season is Summer"
	print(summer)

elif month in ['September', 'October', 'November']:
	fall= "The season is Fall"
	print(fall)

else:
	print("Error! You did not type a valid month.")



"""2. Write a Python program to find the median of three numbers entered by a user."""


def flower(a,b,c):
    if a<=b<=c or c<=b<=a:
        return b
    elif b<=a<=c or c<=a<=b:
        return a
    else:
        return c


a=int(input("Please enter the 1st number: "))
b=int(input("Please enter the 2nd number: "))
c=int(input("Please enter the 3rd number: "))
print("The median is " , flower(a,b,c))



		

"""Write a Python program using print statement to print out a triangle below.
   		*
     *  *  *
  *  *  *  *  *

"""

for coloumn in range(0,4):
		if (coloumn ==1):
			print("    *")
		elif (coloumn==2):
			print("  * * *")
		elif (coloumn==3):
			print("* * * * *")
		else:
			print()



"""
4.  Write a program using conditional statements and user input function to generate the outcome of the rock, scissors, paper game. An example program looks as follows: (texts in blue are inputs from the user). The only valid inputs are rock, paper, and scissors. If the user enters anything else, your program should output “invalid input”.


Player 1: rock
Player 2: paper
Player 2 wins

"""

player_1 = input("Player 1 Choose rock, paper, or scissors ")
player_2 = input("Player 2 Choose rock, paper, or scissors ")

if (player_1 == 'rock' and player_2 == 'scissors'):
	print("Player 1 wins.")

elif (player_1 == 'scissors' and player_2 == 'rock'):
	print("Player 2 wins.")

elif (player_1 == 'rock' and player_2 == 'paper'):
	print("Player 2 wins")

elif (player_1 == 'paper' and player_2 == 'rock'):
	print("Player 1 wins")

elif (player_1 == 'scissors' and player_2 == 'paper'):
	print("Player 1 wins")

elif (player_1 == 'paper' and player_2 == 'scissors'):
	print("Player 2 wins")

elif (player_1 == 'rock' and player_2 == 'rock'):
	print("Tied")
elif (player_1 == 'scissors' and player_2 == 'scis'):
	print("Tied")
elif (player_1 == 'paper' and player_2 == 'paper'):
	print("Tied")
else:
	print("Invalid input")



























