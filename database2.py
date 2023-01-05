import random
import time
import json

alphabets = "abcdefghijklmnopqrstuvwxyz"
numbers = "1234567890"

characters = alphabets + numbers + alphabets.upper()

db = {
	1: {
		"name": "Michael Joshua", 
		"age": 12,
		"stack": ["Python",  "JavaScript"], 
		"password": "1234"
	}, 
	2: {
		"name": "Joshua Michael", 
		"age": 16, 
		"stack": ["BASIC", "Python"], 
		"password": "0000"
	}, 
	3: {
		"name": "Zion Michael", 
		"age": 23, 
		"stack": ["HTML"], 
		"password": "2368"
	}
}


def signup():
	name = input('Enter name: ')
	confirm_age = True
	while confirm_age:
		try:
			age = int(input('Enter age: '))
			confirm_age = False
		except:
			print('enter age in figure')
			
	stack = input('Enter stacks: ')
	
	stack2 = [i for i in stack.split(", ")]
		
	recent_id =[i for i in db.keys()]
		
	print('here are some suggested password for you below')
	choose_password = 0
	while choose_password < 3:
		time.sleep(1)
		password = random.choices(characters,  k=8)
			
		output = "".join(password)
		print(output)
		choose_password += 1
		
	while True:
			print('you can choose from the suggested password above')
			pass1 = input('Enter password: ')
			pass2 = input('confirm password: ')
			if pass1 == pass2:
				
				break
								
	user = {recent_id[-1]+1:{
	'name':name ,
	'age':age ,
	'stacks':stack2,  
	'password':pass2}}
	db.update(user)
	json_data = json.dumps(db, indent = 2)
	print(json_data)
	print('you have successfully signed up')
	print('you can proceed to login')

def signin():
	check_password = True
	
	retries = 0
	
	while check_password:
		if retries < 2:
			username = input('Enter username: ')
			password = input('Enter password: ')
			
			for i in db.values():
				if i['name'] == username and i['password'] == password:
					print('login successful')
					check_password = False
					break
			else:
				print('incorrect password')
	
		else:
			for j in db.items():
				if j[1]['name'] == username:
					db.pop(j[0])
					print(db)
					break
			break
			
		retries += 1

mode = input('sign in or sign up: ')
if mode == 'sign up':
	signup()
	print('would you like to sign in')
	when = input('Now or Later : ').title()
	if when == 'Now':
		signin()
	elif when == 'Later':
		print('thanks for signing up')

#login
elif mode == 'sign in':
	signin()