
# Factorial using recursion
def factorial(n: int) -> int:
  if n == 0:
    return 1
  return n * factorial(n - 1)
  
factorial(5)


def add(a: int, b: int) -> int:
  return a + b

#try:  
#  a = int(input("Enter a: "))
#  b = int(input("Enter b: "))
#  sum = add(a,b)
#  print(sum)
#  
#except ValueError:
#  print("Enter a valid interger")
#  
# Maximum between two numbers
#a = 5
#b = 9
#max = a if a > 5 else b
#print(max)

def order(x: int) -> int:
  n = 0
  while x != 0:
    n += 1
    x = x // 10
  return n
  
def power(x: int, y: int) -> int:
  if y == 0:
    return 1
  sim = power(x, y // 2)
  if y % 2 == 0:
    return sim * sim
  return x * sim * sim
  
def armstrong(x: int) -> bool:
  n = order(x)
  temp = x
  sum = 0
  while temp != 0:
    sum = sum + power(temp % 10, n)
    temp = temp // 10
  return sum == x
  
print(armstrong(1253))

# Prime numbers within a range
def prime(x: int) -> int:
  if x == 1 or x == 0:
    return False
  if any(x % i == 0 for i in range(2,int(x**0.5) + 1)):
    return False
  return True
  
def check_prime(x: int, y: int) -> list:
   p = [n for n in range(x,y + 1) if prime(n)]
   return p
 
print(check_prime(1,1000))

# Fibonacci using recursion
def fibo(x: int) -> int:
   if x == 1:
     return 0
   if x == 2:
     return 1
   return fibo(x - 1) + fibo(x - 2)
print(fibo(10))


ch = "a"
print(ord(ch))
print(type(ord(ch)))
       