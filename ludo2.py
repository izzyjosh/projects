import random
import time


class ludo:
	def player1():
		dice1 = random.randrange(1, 7)
		dice2 = random.randrange(1, 7)
		print('player one')
		print((dice1, dice2))
		return dice1 + dice2
			
	def player2():
		dice3 = random.randrange(1, 7)
		dice4 = random.randrange(1, 7)
		print('player two')
		print((dice3, dice4))
		return dice3 + dice4
		
score = [0, 0]
		
while True:
	time.sleep(1)	
	p1 = ludo.player1()
	time.sleep(1)
	p2 = ludo.player2()
	
	if p1 > p2:
		score[0] += 1
		if score[0] > 5:
			break
	elif p1 < p2:
		score[1] += 1
		if score[1] > 5:
			break
	
	time.sleep(1)
	print("Score: ", "player1",  score, 'player2')