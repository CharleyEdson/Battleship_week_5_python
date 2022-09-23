from board import Board


game_one = Board()
#game_one.start_game()
board = game_one.create_board()
board[0][2] = 2
print(board)

