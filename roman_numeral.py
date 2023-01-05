singles = { "i": 1, 
          "v":5, 
          "x":10, 
          "l":50, 
          "c":100, 
          "d":500, 
          "m":1000}
doubles = {"iv":4, 
                    "ix":9, 
                    "xl":40, 
                    "xc":90, 
                    "cd":400, 
                    "cm":900}
values = 0
num = "xxxiv"
arr = [i for i in num]
for i in range(0, len(num), 1):
	if num[i:i+2] in doubles:
		values += doubles[num[i:i+2]]
		arr.remove(num[i])
		arr.remove(num[i+1])
for i in arr:
	values += singles[i]
print(values)