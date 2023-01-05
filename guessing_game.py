import random


def help():
	print("\tINSTRUCTIONS")
	print('''The game has three levels
level1: you are to guess a number between 0 to 4 with 3 trials
level2: you are to guess a number between 0 to 10 with 5 trials
level3: you are to guess a number between 0 to 16 with 7 trials

if your guess is correct,  you move to the next level
if you failed at level 2 or 3 u will be taken to the previous level

Enjoy your play\n\n''')

help()


def level1():
	print("LEVEL 1")
	try:	
		guess_count = 0
		guess_number = random.randrange(0,  4)
		while guess_count < 3:
			user_guess = int(input("Guess a number : "))
			
			if user_guess == guess_number:
				print("Correct")
				level2()
				break
			else:
				print("Incorrect")
			
			guess_count += 1
		else:
			level1()
			
	except ValueError:
		level1()
		
		
def level2():
	print("LEVEL 2")
	try:	
		guess_count = 0
		guess_number = random.randrange(0,  10)
		
		while guess_count < 5:
			user_guess = int(input("Guess a number : "))
			
			if user_guess == guess_number:
				print("Correct")
				level3()
				break
			else:
				print("Incorrect")
			
			guess_count += 1
		else:
			level1()
	except ValueError:
		level2()


def level3():
	print("LEVEL 3")
	try:	
		guess_count = 0
		guess_number = random.randrange(0,  16)
		
		while guess_count < 7:
			user_guess = int(input("Guess a number : "))
			
			if user_guess == guess_number:
				print("Correct")
				print("Congratulation you completed all the levels.")
				break
			else:
				print("Incorrect")
			
			guess_count += 1
		else:
			level2()
	except ValueError:
		level3()

level1()