# Accept a command to determine the size of the table (rows and columns)


rows = 9
columns = 9
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
def Update_Board(endpoint_pair, count):
  board[endpoint_pair.endpoint1.x][endpoint_pair.endpoint1.y] = count
  board[endpoint_pair.endpoint2.x][endpoint_pair.endpoint2.y] = count

def main():  
  init_board(rows, columns)

  endpoint_coordinates = [
    ((0, 0), (2, 2)),
    ((0, 2), (2, 0)),
  ]

  for pair_number, (first_coords, second_coords) in enumerate(endpoint_coordinates, start=1):
    endpoint1 = Endpoint(*first_coords)
    endpoint2 = Endpoint(*second_coords)
    endpoint_pair = Endpoint_Pair(endpoint1, endpoint2)
    Update_Board(endpoint_pair, str(pair_number))

  for row in board:
      print(' '.join(row))

if __name__ == "__main__":
  main()