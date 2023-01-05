import random

def help():
	print("\tINSTRUCTIONS")
	print('''you are to choose from "ROCK, PAPER, SCISSORS"
ROCK wins against SCISSORS
SCISSORS wins against PAPER
PAPER wins against ROCK\n\n''')


def computer():
	arr = ["rock", "paper", "scissors"]
	choice = random.choice(arr)
	print(f"computer: {choice}\n")
	return choice
	
def player1():
	option = input("player1: ").lower()
	return option
	
def check_winner(b, a):
	computer_score = 0
	player1_score = 0
	tie = 0
	if a == "rock" and b == "scissors":
		computer_score += 1
	elif b == "rock" and a == "scissors":
		player1_score += 1
	elif a == "paper" and b == "rock":
		computer_score += 1
	elif b == "paper" and a == "rock":
		player1_score += 1
	elif a == "scissors" and b == "paper":
		computer_score += 1
	elif b == "scissors" and  a == "paper":
		player1_score += 1
	elif a == b:
		tie += 1
	
	return [computer_score, player1_score, tie]

		
help()

count = 0
com_score = 0
player_score = 0
	
while count < 5:
	game = check_winner(player1(), computer())
	count += 1
	if game[0] == 1:
		com_score += 1
	elif game[1] == 1:
		player_score += 1
	elif game[-1] == 1:
		pass


print("\tSCORE")
print(f"computer : {com_score} \nplayer1 : {player_score} \n")

if com_score > player_score:
	print("computer won")
elif player_score > com_score:
	print("player1 won")
else:
	print("its a tie")
	