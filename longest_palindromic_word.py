#write a code to return the longest palindromic word in an inputed string


#using another function or two function

#this function check if the parsed string is a palindromic word

def palindrom(insert):
	if len(insert) == 0 or len(insert) == 1:
		return True
		
	elif insert[0]  == insert[-1]:
		return palindrom(insert[1:-1])
				
	return False
	
#this function check combination of all letters in the string and parse it to the palindrom function to check if it is a palindromic word
#if the word is palindrom it append it to arr
def pal(word:str) -> str:
	arr =[]
	for i in range(0, len(word)-1):
		for j in range(len(word)-1, 0, -1):
			if word[i] == word[j]:
				pal = palindrom(word[i:j+1])
				if pal == True:
					arr.append(word[i:j+1])
					
#this part check for the longest word in the arr containing word that are palindrom
	max = arr[0]
	for i in range(len(arr)):
		if len(arr[i]) > len(max):
			max = arr[i]
	print(arr)
	print(max)
	
word = input("word: ")
pal(word)



#or for easy coding use this
#a shorter method

arr = []
n = "aaagdjsndjdbabababababajdjdns"
for i in range(len(n)):
	for j in range(len(n)-1, i, -1):
		m = n[i:j+1]
		if m[::] == m[::-1]:	
			arr.append(m)
max = arr[0]
for i in arr:
	if len(i) > len(max):
		max = i
		
print(max)