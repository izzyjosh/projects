def questions():
	print("\tQUESTIONS")
	Q1 = input('Q1: who wrote python? ').lower()
	while True:
		try:
			Q2 = int(input("Q2: what year was python written? "))
			break
		except ValueError:
			print("it should be a number not a character")
	Q3 = input("Q3: who is the world richest man? ").lower()
	Q4 = input("Q4: is python an OOP language? ").lower()
	Q5 = int(input("Q5: 2 + 2 = "))
	return [Q1, Q2, Q3, Q4, Q5]


def help():
	print("\tINSTRUCTIONS")
	print('''Answer each question correctly
Each question takes one mark 
Try your best to score more than average\n\n''')

		
						
def remark(score):
	if score > 0 and score <= 25:
		print("poor performancell put more effort :(")
	elif score > 25 and score <= 49:
		print("almost there!! try harder :(")
	elif score > 49 and score <= 75:
		print("great performance!! keep it up :)")
	elif score > 75 and score <= 100:
		print("outstanding performance!! the sky is your limit :)")
		
		 	 	
def answer():
	return ["joshua", 1991, "elon musk", "yes", 4]
	
	
def game():
	
	score = 0
	question = questions()
	ans = answer()
	print("\n\n")
	print("\tRESULT STATS")
	
	
	for i in range(len(question)):
		if question[i] == ans[i]:
			print(f"Q{i+1}: correct")
			score += 1
		else:
			print(f"Q{i+1}: incorrect")
			
	print("\n\n")
	print(f"Dear {name} you scored {score} out of {len(question)} question")
	percent = score * 100 / len(question)
	print("\n")
	print(f"percentage = {percent}%")
	remark(int(percent))




name = input("name: ").upper()
ask = input(f"{name} Do You Want To Play Quiz Game ? ").upper()
print("\n")
if ask == "YES":
	help()
	print(f"WELCOME TO QUIZ GAME {name}")
	print("\n\n")
	game()
else:
	quit()