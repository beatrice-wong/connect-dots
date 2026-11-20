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
      
# class for the endpoints of the table
class Endpoint:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    
  # update the coordinates of the endpoint
  def set_coordinates(self, x, y):
    self.x = x
    self.y = y

class Endpoint_Pair:
  def __init__(self, endpoint1, endpoint2):
    self.endpoint1 = endpoint1
    self.endpoint2 = endpoint2
    
# update board with the endpoint pair
def Update_Board(endpoint_pair):
  board[endpoint_pair.endpoint1.x][endpoint_pair.endpoint1.y] = 'P1'
  board[endpoint_pair.endpoint2.x][endpoint_pair.endpoint2.y] = 'P2'

def main():
  
  
  init_board(rows, columns)
  for row in board:
    print(' '.join(row))
    
  P1 = Endpoint(0, 0)
  P2 = Endpoint(2, 2)
  endpoint_pair = Endpoint_Pair(P1, P2)
  Update_Board(endpoint_pair)

  for row in board:
      print(' '.join(row))

if __name__ == "__main__":
  main()