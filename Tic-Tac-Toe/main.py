from enum import Enum

board = []
rows = cols = 3

for i in range(rows):
  row = []
  for j in range(cols):
    row.append(' ')
  board.append(row)

class Choice(Enum):
  Cross = 'X'
  Circle = 'O'

def display_board(game):
  print()
  for i in range(rows):
    for j in range(cols):
      if (j == 0):
        print(f"{game[i][j]} ", end=" ")
      else:
        print(f"| {game[i][j]} ", end=" ")
    print()


def winner(player, game):
  print()
  print(player.value, "is the winner")
  display_board(game)


def check_for_win(game, player):
  result = 0
  #checking for the rows
  winner_found = False
  for i in range(rows):

    for j in range(cols):
      if (game[i][j] == player.value):
        result += 1
        if result == 3:
          winner(player, game)
          winner_found = True
          break

    if (winner_found):
      break
    result = 0

    for k in range(cols):
      if (game[k][i] == player.value):
        result += 1
        if result == 3:
          winner(player, game)
          winner_found = True
          break

    if (winner_found):
      break
    result = 0

    if game[0][0] and game[1][1] and game[2][2] == player.value:
      winner(player, game)
      winner_found = True
      break
    if game[0][2] and game[1][1] and game[2][0] == player.value:
      winner_found = True
      winner(player, game)
      break


def printGame(game, player, position):
  board_position = 0
  for i in range(rows):
    for j in range(cols):
      board_position = board_position + 1
      #print(board_position)
      if (board_position == int(position)):
        game[i][j] = player.value
      if (j == 0):
        print(f"{game[i][j]} ", end=" ")
      else:
        print(f"| {game[i][j]} ", end=" ")
      check_for_win(game, player)
    print()


class Players:
  user1 = 1
  user2 = 2

  @classmethod
  def set_user_choices(cls, choice):
    choice = int(choice)
    if choice == 1:
      cls.user1 = Choice.Cross
      cls.user2 = Choice.Circle
    else:
      cls.user1 = Choice.Circle
      cls.user2 = Choice.Cross

  @classmethod
  def get_user_choice(cls, player):
    if player == 1:
      return cls.user1
    else:
      return cls.user2

def play():
  choice_selection = input("Press 1 for X or 2 for O : ")
  Players.set_user_choices(choice_selection)
  print()

  for i in range(1, 10):
    player_position = input("Select a postion from one to Nine : ")
    player = Players.get_user_choice(
        1) if i % 2 == 1 else Players.get_user_choice(2)
    printGame(board, player, player_position)
    print()

play()
