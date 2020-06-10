
gameBoard = { '1': ' ', '2': ' ', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': ' ', '8': ' ', '9': ' ' }


def printBoard(board):


	print(board['7'] +'|'+ board['8'] +'|'+ board['9'])
	print('-----')
	print(board['4'] +'|'+ board['5'] +'|'+ board['6'])
	print('-----')
	print(board['1'] +'|'+ board['2'] +'|'+ board['3'])
	

newBoard = []

for key in gameBoard:
    newBoard.append(key)


def game():

	turn = 'X'
	count = 0

	# names = []
	# for i in range(2):
	# 	z = input("enter your name : ")
	# 	names.append(z)

	for i in range(9):
		printBoard(gameBoard)
		print('\n'+ 'its your turn' + ' ' + turn + ' ' + '\n'+'Enter your choice: ')

		move = input()
		print(end = '\n')

		if gameBoard[move] == ' ':
			gameBoard[move] = turn
			count += 1

		else:
			print('the place is already filled, enter another location: ')
			continue

		if count >= 5:
			if gameBoard['7'] == gameBoard['8'] == gameBoard['9'] != ' ':
				printBoard(gameBoard)
				print('*-------GAME OVER-------*')
				print(turn + ' won the game :-)')
				break

			elif gameBoard['4'] == gameBoard['5'] == gameBoard['6'] != ' ':
				printBoard(gameBoard)
				print('*-------GAME OVER-------*')
				print(turn + ' won the game :-)')
				break

			elif gameBoard['1'] == gameBoard['2'] == gameBoard['3'] != ' ':
				printBoard(gameBoard)
				print('*-------GAME OVER-------*')
				print(turn + ' won the game :-)')
				break

			elif gameBoard['1'] == gameBoard['4'] == gameBoard['7'] != ' ':
				printBoard(gameBoard)
				print('*-------GAME OVER-------*')
				print(turn + ' won the game :-)')
				break

			elif gameBoard['2'] == gameBoard['5'] == gameBoard['8'] != ' ':
				printBoard(gameBoard)
				print('*-------GAME OVER-------*')
				print(turn + ' won the game :-)')
				break

			elif gameBoard['3'] == gameBoard['6'] == gameBoard['9'] != ' ':
				printBoard(gameBoard)
				print('*-------GAME OVER-------*')
				print(turn + ' won the game :-)')
				break

			elif gameBoard['7'] == gameBoard['5'] == gameBoard['3'] != ' ':
				printBoard(gameBoard)
				print('*-------GAME OVER-------*')
				print(turn + ' won the game :-)')
				break

			elif gameBoard['1'] == gameBoard['5'] == gameBoard['9'] != ' ':
				printBoard(gameBoard)
				print('+*------GAME OVER-------*')
				print(turn + ' won the game :-)')
				break

		if count == 9:
			print("GAME OVER")
			print("The game was a Tie.")



		if turn == 'X':
			turn = '0'
		else:
			turn = 'X'

	print("DO you wish to play again")
	restart = input("Enter Y/y for yes and N/n for no: ")


	if restart == 'Y' or restart == 'y':

		for keys in newBoard:
			gameBoard[keys] = ' '
		
		game()


if __name__ == "__main__":
	game()




