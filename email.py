#this project is just a demo on how back end of most login and signup process occurs 


import re
import random



def signup():
	numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
	
	
	last_name = input("last name  ").upper()
	first_name = input("\tfirst name  ").upper()
	middle_name = input("\t\tmiddle name  ").upper()
	
	try:
		age = int(input("Age  "))
	except ValueError:
		print("\tit should be a valid number")
	gender = input("gender (Male) or (Female)  ").upper()
	phone_number = int(input("\tphone number  "))
	
		
	rand = random.choices(numbers, k = 6)
	print("verification code "+ str(rand))
	
	verify = input("\tenter the code  ")
	arr = [int(i) for i in verify]
	
	
	while True:
		if arr == rand:
		
			user_email = input("choose an email name   ").lower()
			user_password = input("choose password  ")
			confirm_password = input("\tconfirm password  ")
	
			if confirm_password == user_password:
				file = open("/storage/emulated/0/email.txt", "a")
				writing_file = file.write(f"\n{last_name} {middle_name} {first_name}, {age}, {gender},  +234{phone_number},  {user_email}@gmail.com,  {user_password}")
				file.close()
				break
					
			else:
				print("\tboth of the password should be equal")
	
			
		else:
			print("make sure you copy the code above")
			break
			
		
def login():		
	users_email = []
	
	email = input("enter email: ")
	password = input("enter password: ")
	
	
	
	file = open("/storage/emulated/0/email.txt", "r")
	read_file = file.read()
	
	
	contents_of_file = [[j.strip() for j in i .split(", ")]  for i in read_file.split("\n")]
	print(contents_of_file)
	
	
	pattern = re.compile(r"[a-zA-Z0-9]+@[a-z]+\.[a-z]+")
	matches = pattern.finditer(read_file)
	
	
	for match in matches:
		users_email.append(match.group())
		
		
	for email_address in users_email:
		if email_address ==  email:
			for content  in contents_of_file:
				if content[-1] == password:
					print("successful")
					break
			break
			
	else:
		print("invalid email address or password")
		
		
def mode():		
	modes = input("enter (login) or (signup): ").lower()
	return modes
	
	
count  = 0
mod = mode()
while True:
	if mod == "login":
		login()
		break
	elif mod == "signup":		
		signup()
		login()
		break
	else:
		print("i dont understand this")
		print(mode())