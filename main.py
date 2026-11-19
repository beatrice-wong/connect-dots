# Accept a command to determine the size of the table (rows and columns)


rows = 3
columns = 3
coords = []
board = []

# visualise the table and allocate coordinates to each endpoint    
def init_board(rows, columns):
  for i in range(rows):
    row = []
    for j in range(columns):
      row.append('.')
    board.append(row)
    
  for i in range(rows):
    for j in range(columns):
      coords.append((i, j))
  
def main():
  init_board(rows, columns)
  for row in board:
    print(' '.join(row))

if __name__ == "__main__":
  main()