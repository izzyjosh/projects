import logic 

if __name__ == "__main__":
  mat = logic.start_game()
  print("\n=== start ===")
  for i in range(4):
    print(mat[i], end="\n")
 
while True:
  x = input("Enter the command: ").lower()
  
  if x == "w":
    mat, flag = logic.move_up(mat)
    status = logic.game_state(mat)
    if status == "won" or status == "lost":
      print(status)
    
    if status != "Game not over":
      break
    logic.add_new_2(mat)
    
  elif x == "a":
    mat, flag = logic.move_left(mat)
    status = logic.game_state(mat)
    if status == "won" or status == "lost":
      print(status)
    
    if status != "Game not over":
      break
    logic.add_new_2(mat)
  
  elif x == "d":
    mat, flag = logic.move_right(mat)
    status = logic.game_state(mat)
    if status == "won" or status == "lost":
      print(status)
    
    if status != "Game not over":
      break
    logic.add_new_2(mat)
    
  elif x == "s":
    mat, flag = logic.move_down(mat)
    status = logic.game_state(mat)
    if status == "won" or status == "lost":
      print(status)
    
    if status != "Game not over":
      break
    logic.add_new_2(mat)
    
  else:
    print("Invalid command")
      
  for i in range(4):
    print(mat[i], end="\n")