#------------------------------------------------------------------------------
def is_XO(board):
	'''
	checks if elements of the board are indeed 'X' or 'O' (or ' ') ONLY!

	:param {String[]} board : is a list of length 9 each corresponding to a 
	loaction on the tic-tac-toe board. elements of the list shouldbe either 
	'X' or 'O'
	'''
	for mark in board:
		if mark != 'X' and mark != 'O' and mark != ' ':
			return False
	return True


def print_board(board):
	'''
	prints the tic-tac-toe board and indicates the marked locations

	:param {String[]} board : is a list of length 9 each corresponding to a 
	loaction on the tic-tac-toe board. elements of the list should be either 
	'X' or 'O' (or ' ')
	'''
	assert len(board) == 9
	assert is_XO(board)
	print("     |     |      ")
	print("  {}  |  {}  |  {}  ".format(board[0], board[1], board[2]))
	print("_____|_____|_____")
	print("     |     |     ")
	print("  {}  |  {}  |  {}  ".format(board[3], board[4], board[5]))
	print("_____|_____|_____")
	print("     |     |     ")
	print("  {}  |  {}  |  {}  ".format(board[6], board[7], board[8]))
	print("     |     |     ")


def set_markers():
	"""
	assigns 'X' or 'O' to each player.

	:return {Dictionary} : mapping from {"player1", "player2"} to {'X', 'O'}  
	"""
	marker = {"player1" : 'X', "player2" : 'O'}
	while True :
		player1_mark = input("Player 1: Do you want to be 'X' or 'O'? ")
		if player1_mark == 'X':
			break
		elif player1_mark == 'O':
			marker["player1"] = 'O'
			marker["player2"] = 'X'
			break
		else :
			print("You must chose between 'X' and 'O' ONLY!")
	return marker


def begin_play():
	"""
	player option to start the game or not.

	:return {boolean} : True to start the game. False to terminate play.
	"""
	while True :
		play = input("Are you ready to play? Enter YES or NO. ")
		if play == 'YES':
			return True
		elif play == 'NO':
			return False
		else :
			print("Please enter a YES or NO only!")


def get_postion(pointer):
	"""
	player option to select position to place his/her mark.

	:param {string} pointer : possible values "player1" and "player2"

	:return {int} position : between 1-9 correspoing to position on the board
	"""
	while True :
		position = int(input("Choose your next position {} : (1-9) ".format(pointer)))
		if position >= 1 and position <= 9:
			return position
		else :
			print("Invalid position! Try again!")



def check_game(board, last_move):
	"""
	check if any player has managed to get 3 marks in a row, column or diagonally.

	:param {String[]} board : current board with marker locations of both players
	:param {int} last_move : between 1-9 where the most recent marker was put.

	:return {Boolean} : True if player who played "last_move" has won. False otherwise
	"""
	win = ["012","345", "678", "036", "147", "258", "048", "246"]
	win = list(filter(lambda string : str(last_move) in string, win))
	for x in win:
		if board[int(x[0])] == board[last_move]:
			if board[int(x[1])] == board[last_move]:
				if board[int(x[2])] == board[last_move]:
					return True
	return False


def game():
	"""
	The application where all the user inputs are managed. Board is 
	printed after each move. The outcome of the game is printed.
	"""
	print("Welcome to Tic Tac Toe!")
	marker = set_markers()
	print("Player 1 will go first.\n")
	pointer = "player1"
	board = [' ']*9;
	play = begin_play()
	move_counter = 0
	while play == True :
		print_board(board)
		while True:
			position = get_postion(pointer)
			if board[position-1] == ' ':
				board[position-1] = marker[pointer]
				move_counter += 1
				break
			else:
				print("Can't put marker here! Try again!")

		game_over = check_game(board, position-1)
		if game_over == True:
			print_board(board)
			print("Congratulations! {} has won!".format(pointer))
			break
		elif move_counter == 9:
			print("Game is a draw!")
			break
		else:
			if pointer == "player1":
				pointer = "player2"
			else:
				pointer = "player1"


game()