import random

def get_word():
  words = "mango apple orange pineapple banana peer watermelon grape cherry lime date"
  return random.choice(words.split(" "))

def give_feedback(word, user_guess, user_progress):
  found = False
  for i, ch in enumerate(word):
    if ch == user_guess and user_progress[i] == "_":
      user_progress[i] = ch
      found = True
  return found


def Hangman():
  print("""=== Welcome to Hangman Game ===
- You are to guess a letter in each trial
- You have length of word plus two trials to guess the word\n""")
  
  # Get the word to be guessed  
  word = get_word()
  user_progress = ["_" for _ in range(len(word))]
  
  print("Guess the word: Hint, word is a fruit")
  print(" ".join(user_progress), end="\n\n") 
  
  # Get user input
  trials = len(word) + 2
  
  for attempt in range(trials):
    print(f"Attempts left: {trials - attempt}")
    
    user_guess = input("Enter a letter to guess: ").lower()
    
    # Check user input
    if len(user_guess) != 1 or not user_guess.isalpha():
      print("Invalid input, please enter a single letter")
      continue
             
    # Feedback 
    give_feedback(word, user_guess, user_progress)
          
    print(" ".join(user_progress), end="\n\n")
    
    if "".join(user_progress) == word:
      print("Congratulations!!, You won")
      break
      
  else:
    print(f"You loose, the word was {word.upper()}")
    
if __name__ == "__main__":
  Hangman()