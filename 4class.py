""" Class 4""" 
if expression:
	statement 1
	statement 2
	...

if expression:
	statement 1
	statement 2

else:
	statement 3
	statement 4

User-defined functions
syntax:
def functionName ():
	statement 1
	statement 2


def countdown (n):
	if n<=0:
		print("Blastoff!")
	else:
		print(n)
		countdown(n-1)
n=0


Recursion
n!= n* (n-1) * (n-2)...1
def factorial(n):
	if n==1:
		return 1
	else:
		return n*factorial(n-1)

"""range will tell you when to start and when to stop
you can also tell how to do a step by (start, stop, step)"""

range(start,stop):

range(5)
[0,1,2,3,4]

range(5,10)
[5,6,7,8,9]

range(0,10,2)
[0,2,4,6,8]

"""
The for loop

Repeats a set of statements over a group of values."""


for i in range(5):
	print('i is now:', i)

for x in range(1,6):
	print(x, "squared is", x*x)

for friend in['Alice','Bryan', 'Chris']:
	invitation = "Hi " + friend + ". Please join my party on Saturday!"
	print(invitation)


sum=0
for i in range (1,11):
	sum = sum+ i*i 
print("The sum of the first 10 scores is", sum)



factorial = 1
n= int(input("Please enter an integar: "))
for i in range(n+1):
	factorial = factorial*i
	i=i+1
print("The factorial of n is", factorial)


rite code to print the pattern L



#for row in range(0,5):
for coloumn in range(0,7):
		if (coloumn ==1 or coloumn==3 or coloumn==5):
			print("*")
		elif (coloumn==2 or coloumn==4):
			print(" ")
		elif (coloumn==6):
			print("*****")
		else:
			print()
	


x=15
if x<2:
	print("Below 2")
elif x<20:
	print("Below 20")
elif x<10:
	print("Below 10")
else:
	print("Something else")




















