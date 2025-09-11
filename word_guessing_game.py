import random
from wordfreq import top_n_list

def get_word() -> str:
  # Generate the word
  word_list = top_n_list("en", 5000)
  filtered_words = [w for w in word_list if 4 <= len(w) <= 5]
  return random.choice(filtered_words)
  
def give_feedback(word: str, guess: str):
  green = sum(w == g for w,g in zip(word, guess))
  
  word_remaining = []
  guess_remaining = []
  
  for w, g in zip(word, guess):
    if w != g:
      word_remaining.append(w)
      guess_remaining.append(g)
  
  yellow = sum(min(guess_remaining.count(c), word_remaining.count(c)) for c in set(guess_remaining))
  
  return green, yellow
  
def play_game():
  print("""\n === Instructions ===
  - This is a word guessing game
  - Green: letters in the correct position
  - Yellow: letters in the wrong position
  - Trials: you onlh have five trials """)
  
  word = get_word()
  word_length = len(word)
  print(f"\n=== The word has {word_length} letters ===\n")
  
  trials = 1
  while trials <= 5:
    user_guess = input(f"Attempts {trials}/5 \n Enter a {word_length}-letter word: ").lower().strip()
    
    if len(user_guess) != word_length:
      print(f"Please enter exactly {word_length} letters \n")
      continue
      
    green, yellow = give_feedback(word, user_guess)
    
    if user_guess == word:
      print(f"Congratulations!!!, you guessed the word: {word.upper()}")
      break
      
    print(f"{green} green | {yellow} yellow")
    
    trials += 1   
     
  else:
    print(f"Out of tries!!, The word was: {word.upper()}")
    
if __name__ == "__main__":
  play_game()