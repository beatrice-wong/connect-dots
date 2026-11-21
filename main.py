# Accept a command to determine the size of the table (rows and columns)

rows = 9
columns = 9
coords = []
board = []

# visualise the table and allocate coordinates to each endpoint    
def init_board(rows, columns):
  board.clear()
  coords.clear()
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

def Parse_Endpoint_Pair(value):
  parts = value.replace(",", " ").replace("(", " ").replace(")", " ").split()
  if len(parts) != 4:
    raise ValueError("Expected two coordinates: x1 y1 x2 y2")

  try:
    numbers = [int(part) for part in parts]
  except ValueError:
    raise ValueError("Coordinates must be whole numbers")

  first = (numbers[0], numbers[1])
  second = (numbers[2], numbers[3])
  return first, second

def Input_Endpoint():
  while True:
    try:
      pair_count = int(input("Enter the number of endpoint pairs: "))
      if pair_count < 1:
        print("Please enter at least one endpoint pair.")
        continue
      break
    except ValueError:
      print("Please enter a whole number.")

  endpoint_coordinates = []
  for pair_number in range(1, pair_count + 1):
    while True:
      value = input(
        f"Enter endpoint pair {pair_number} as x1 y1 x2 y2 "
        "(for example, 0 0 2 2): "
      )
      try:
        first, second = Parse_Endpoint_Pair(value)
      except ValueError as error:
        print(error)
        continue

      if not (0 <= first[0] < rows and 0 <= first[1] < columns
              and 0 <= second[0] < rows and 0 <= second[1] < columns):
        print(f"Coordinates must be between (0, 0) and ({rows - 1}, {columns - 1}).")
        continue

      endpoint_coordinates.append((first, second))
      break

  return endpoint_coordinates
    
# update board with the endpoint pair
def Update_Board(endpoint_pair, count):
  board[endpoint_pair.endpoint1.x][endpoint_pair.endpoint1.y] = count
  board[endpoint_pair.endpoint2.x][endpoint_pair.endpoint2.y] = count

def main():  
  init_board(rows, columns)
  endpoint_coordinates = Input_Endpoint()

  for pair_number, (first_coords, second_coords) in enumerate(endpoint_coordinates, start=1):
    endpoint1 = Endpoint(*first_coords)
    endpoint2 = Endpoint(*second_coords)
    endpoint_pair = Endpoint_Pair(endpoint1, endpoint2)
    Update_Board(endpoint_pair, str(pair_number))

  for row in board:
      print(' '.join(row))

if __name__ == "__main__":
  main()