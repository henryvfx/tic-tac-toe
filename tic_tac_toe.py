
import random

board = [[' ' for _ in range(3)] for _ in range(3)]

players = ['X', 'O']

current_player = 0

def display_board():
  print(f' {board[0][0]} | {board[0][1]} | {board[0][2]} ')
  print('-----------')
  print(f' {board[1][0]} | {board[1][1]} | {board[1][2]} ')
  print('-----------')
  print(f' {board[2][0]} | {board[2][1]} | {board[2][2]} ')

def check_win(player):
  for row in board:
    if row == [player, player, player]:
      return True
  for col in range(3):
    if board[0][col] == player and board[1][col] == player and board[2][col] == player:
      return True
  if board[0][0] == player and board[1][1] == player and board[2][2] == player:
    return True
  if board[0][2] == player and board[1][1] == player and board[2][0] == player:
    return True
  return False

def check_draw():
  for row in board:
    if ' ' in row:
      return False
  return True

def ai_move():
  empty_spaces = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
  row, col = random.choice(empty_spaces)
  board[row][col] = 'O'

while True:
  display_board()
  
  if current_player == 0:
    row = int(input(f'{players[current_player]}, enter a row (0, 1, 2): '))
    col = int(input(f'{players[current_player]}, enter a column (0, 1, 2): '))
  
    if board[row][col] == ' ':
      board[row][col] = players[current_player]
    else:
      print('That space is already occupied!')
      continue
  else:
    ai_move()

  if check_win(players[current_player]):
    print(f'{players[current_player]} wins!')
    break
  elif check_draw():
    print(f"{players[current_player]} wins!")
  current_player = (current_player + 1) % 2
