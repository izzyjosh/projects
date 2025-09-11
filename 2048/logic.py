import random

def move_down(grid: list):
  # To move down, transpose - move right - transpose again
  new_grid = transpose(grid)
  new_grid, changed = move_right(new_grid)
  new_grid = transpose(new_grid)
  return new_grid, changed

def move_up(grid: list):
  # To move up, transpose - move left - transpose again
  new_grid = transpose(grid)
  new_grid, changed = move_left(new_grid)
  new_grid = transpose(new_grid)
  return new_grid, changed

def move_right(grid: list):
  # reverse first
  new_grid = reverse(grid)
  
  # move left
  new_grid, changed = move_left(new_grid)
  
  # reverse again to vet the desired result
  new_grid = reverse(new_grid)
  return new_grid, changed

# Function to update the mat if we swipe or move left
def move_left(grid: list):
  # Compress first
  new_grid, changed1 = compress(grid)
  # Merge the compress grid
  new_grid, changed2 = merge(new_grid)
  changed = changed1 or changed2
  
  # Compress again if there was a merge
  new_grid, temp = compress(new_grid)
  
  return new_grid, changed


# Function that turns rows into columns
def transpose(mat: list):
  new_mat = []
  for i in range(4):
    new_mat.append([])
    for j in range(4):
      new_mat[i].append(mat[j][i])
  return new_mat

# Function to reverse the content of the matrix
def reverse(mat: list):
  new_mat = []
  for i in range(4):
    new_mat.append([])
    for j in range(4):
      new_mat[i].append(mat[i][3-j])
  return new_mat


# function to merge the cell in matrix after compressing
def merge(mat: list):
  changed = False
  for i in range(4):
    for j in range(3):
      
      # check if the next cell is the same with the current and double if true making the next zero after
      if mat[i][j] == mat[i][j + 1] and mat[i][j] != 0:
        mat[i][j] = mat[i][j] * 2
        mat[i][j + 1] = 0
        changed = True
        
  return mat, changed
  
  
# Function to compress the grid after every step before and after merging cells
def compress(mat: list):
  # Variable to know if there was a change
  changed = False
  
  # New mat
  new_mat = []
  
  # empty
  for i in range(4):
    new_mat.append([0] * 4)
    
  # shift entries of each cell to extreme left
  for i in range(4):
    pos = 0
    
    for j in range(4):
      if mat[i][j] != 0:
        new_mat[i][pos] = mat[i][j]
        
        if j != pos:
          changed = True
        pos += 1
  return new_mat, changed
  

# This function is required tk know the game current state
def game_state(mat: list):
  # If the user has won
  # A cell contains 2048
  if any(any(cell == 2048 for cell in row) for row in mat):
    return "won"
  
  # => The game is not over 
  # If on cell is empty
  if any(any(cell == 0 for cell in row) for row in mat):
    return "Game not over"
        
  # if the cell after and below is the same
  for i in range(3):
    for j in range(3):
      if mat[i][j] == mat[i + 1][j] or mat[i][j] == mat[i][j + 1]:
        return "Game not over"
   
  return "lost"
  

def get_first_empty(mat: list):
  for i in range(4):
    for j in range(4):
      if mat[i][j] == 0:
        return i,j
  return None, None
  
def add_new_2(mat: list):
  # Check infthe matrix is already filled
  if all(all(cell != 0 for cell in row) for row in mat):
    return
  
  # Randomly find an empty cell
  tries = 0
  while tries < 30:
    r = random.randint(0,3)
    c = random.randint(0,3)
    
    if mat[r][c] == 0:
      mat[r][c] = 2
      return
    tries += 1
      
  # If the random method fails too many times get it manually
  r,c = get_first_empty(mat)
  if r is not None and c is not None:
    mat[r][c] = 2
  

def start_game() -> list:
  mat = []
  
  for i in range(4):
    mat.append([0] * 4)
  
  # Commands to use
  print("""=== Use the following commands ===
  - W or w: to move up
  - S or s: to move down
  - A or a: to move left
  - D or d: to move right""")
  
  add_new_2(mat)
  return mat