import random


def print_board(board):
	print()
	for i in range(3):
		row = ' | '.join(board[i*3:(i+1)*3])
		print(' ' + row)
		if i < 2:
			print('---+---+---')
	print()


def available_moves(board):
	return [i for i, v in enumerate(board) if v == ' ']


def check_winner(board):
	wins = [
		(0,1,2),(3,4,5),(6,7,8),
		(0,3,6),(1,4,7),(2,5,8),
		(0,4,8),(2,4,6)
	]
	for a,b,c in wins:
		if board[a] == board[b] == board[c] and board[a] != ' ':
			return board[a]
	if ' ' not in board:
		return 'Tie'
	return None


def player_move(board, player):
	while True:
		try:
			move = input(f"Player {player} - enter move (1-9): ")
			pos = int(move) - 1
			if pos in range(9) and board[pos] == ' ':
				board[pos] = player
				return
			print('Invalid move, try again.')
		except ValueError:
			print('Please enter a number 1-9.')


def minimax(board, depth, is_maximizing, ai_player, hu_player):
	winner = check_winner(board)
	if winner == ai_player:
		return 10 - depth
	if winner == hu_player:
		return depth - 10
	if winner == 'Tie':
		return 0

	if is_maximizing:
		best = -999
		for m in available_moves(board):
			board[m] = ai_player
			score = minimax(board, depth+1, False, ai_player, hu_player)
			board[m] = ' '
			if score > best:
				best = score
		return best
	else:
		best = 999
		for m in available_moves(board):
			board[m] = hu_player
			score = minimax(board, depth+1, True, ai_player, hu_player)
			board[m] = ' '
			if score < best:
				best = score
		return best


def ai_move(board, ai_player, hu_player):
	best_score = -999
	best_move = None
	for m in available_moves(board):
		board[m] = ai_player
		score = minimax(board, 0, False, ai_player, hu_player)
		board[m] = ' '
		if score > best_score:
			best_score = score
			best_move = m
	if best_move is None:
		best_move = random.choice(available_moves(board))
	board[best_move] = ai_player


def choose_game_mode():
	print('Choose game mode:')
	print('1) Human vs Human')
	print('2) Human vs Computer')
	while True:
		choice = input('Enter 1 or 2: ')
		if choice in ('1','2'):
			return int(choice)
		print('Invalid choice.')


def main():
	print('Tic-Tac-Toe')
	while True:
		mode = choose_game_mode()
		board = [' '] * 9
		current = 'X'
		hu_player = None
		ai_player = None
		if mode == 2:
			hu_player = ''
			while hu_player.upper() not in ('X','O'):
				hu_player = input('Choose your mark (X/O): ').upper()
			ai_player = 'O' if hu_player == 'X' else 'X'

		print_board(board)
		while True:
			if mode == 1:
				player_move(board, current)
			else:
				if current == hu_player:
					player_move(board, hu_player)
				else:
					print('Computer is thinking...')
					ai_move(board, ai_player, hu_player)

			print_board(board)
			result = check_winner(board)
			if result:
				if result == 'Tie':
					print("It's a tie!")
				else:
					print(f'Player {result} wins!')
				break
			current = 'O' if current == 'X' else 'X'

		# ask to play again
		while True:
			again = input('Play again? (y/n): ').strip().lower()
			if again in ('y', 'yes'):
				break  # outer loop will restart and re-ask mode
			if again in ('n', 'no'):
				print('Thanks for playing!')
				return
			print('Please enter Y or N.')


if __name__ == '__main__':
	main()

