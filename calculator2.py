#calculator
import math 

chose = input("enter O for (+, -, ×, ÷, %, ^, P, C) or EO for (others): ").upper()

if chose == "O":
	while True:
		try:
			num1 = float(input("first number : "))
			break
		except ValueError:
			print("it should be number please")
			
	sign = input("sign : ")
	
	while True:
		try:
			num2 = float(input("second number : "))
			break
		except ValueError:
			print("it should be number please")
	
	class Operations:
		
		def sum():
			if sign == "+":
				print(f"{num1} + {num2} = ", num1 + num2)
			
		def product():
			if sign == "×":
				print(f" {num1} × {num2} = ", num1 * num2)
				
		def difference():
			if sign == "-":
				print(f"{num1} - {num2} = ", num1 - num2)
				
		def quotient():
			if sign == "÷":
				print(f"{num1} ÷ {num2} = ", num1 / num2)
				
		def modulus():
			if sign == "%":
				print(f"{num1} % {num2} = ", num1 % num2)
				
		def power():
			if sign == "^":
				print(f"{num1} ^ {num2} = ", num1 ** num2)
				
		def comb():
			if sign == "c":
				print(f"{num1} C {num2} = ", math.comb(int(num1), int(num2)))
				
		def perm():
			if sign == "p":
				print(f"{num1} P {num2} = ", math.perm(int(num1), int(num2)))
				
				
	Operations.sum()
	Operations.product()
	Operations.quotient()
	Operations.modulus()
	Operations.difference()
	Operations.power()
	Operations.comb()
	Operations.perm()
	
elif chose == "EO":
	
	sign = input("sign: ")
	
	while True:
		try:
			num1 = float(input("Enter number: "))
			break
		except ValueError:
			print("numbers please")
	
	class ExtraOperation:
		
		def sin():
			if sign == "sin":
				print(f"sin {num1} = ", math.sin(num1))
				
		def cos():
			if sign == "cos":
				print(f"cos {num1} = ", math.cos(num1))
				
		def tan():
			if sign == "tan":
				print(f"tan {num1} = ", math.tan(num1))
				
		def log10():
			if sign == "log10":
				print(f"log10 of {num1} = ", math.log10(num1))
				
		def log2():
			if sign == "log2":
				print(f"log2 of {num1} = ", math.log2(num1))
				
		def root():
			if sign == "√":
				print(f"√{num1} = ", math.sqrt(num1))
				
		def factorial():
			if sign == "!":
				print(f"{num1} ! = ", math.factorial(int(num1)))
				
		
	ExtraOperation.sin()
	ExtraOperation.cos()
	ExtraOperation.tan()
	ExtraOperation.log2()
	ExtraOperation.log10()
	ExtraOperation.root()
	ExtraOperation.factorial()