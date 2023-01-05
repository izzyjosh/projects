import random


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
				break
			else:
				print("Incorrect")
			
			guess_count += 1
		else:
			level2()
	except ValueError:
		level3()

level1()