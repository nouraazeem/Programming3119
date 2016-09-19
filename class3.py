y=2
if y==1:
	print("y still equals 1, I was just checking.")


food= "shrimp"
if food == "shrimp":
	print ("Hmm, my favorite!")
	print ("I am happy.")

#Example 3 if statements


weight = float (input("How many pounds does your suitcase weigh?"))
if weight > 50:
	print("There is a 25$ charge for luggage that heavy.")
	print("Thank you for your business.")
elif weight <49:
	print("You do not have a charge")

"""Sometimes, it is useful to have a body with no statememnt. This is a pass."""


#Example 1:

number = int(input("Please enter a number: "))
if number < 100:
	print("The number is less thn 100.")
else: 
	print("The number is greater than 100.")


i = 10
if i%2 ==0:
	print("Number is even.")
elif i==10:
	print("The number is 10")
else: 
	print("Number is odd.")


x=5
y= 10
if x<y:
	print("x is less than y.")
elif x>y:
	print("x is larger than y.")
else:
	print("x is equal to y.")