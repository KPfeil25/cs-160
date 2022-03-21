def create_board():
    board = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]
    return board

def print_board(board):

    print(' ' + board[0][0] + ' ' + '|' + ' ' + board[0][1] + ' ' + '|' + ' ' + board[0][2] + ' ')
    print('-' + '-' + '-' + '-' + '-' + '-' + '-' + '-' + '-' + '-' + '-')
    print(' ' + board[1][0] + ' ' + '|' + ' ' + board[1][1] + ' ' + '|' + ' ' + board[1][2] + ' ')
    print('-' + '-' + '-' + '-' + '-' + '-' + '-' + '-' + '-' + '-' + '-')
    print(' ' + board[2][0] + ' ' + '|' + ' ' + board[2][1] + ' ' + '|' + ' ' + board[2][2] + ' ')

def get_player_info():
    num_players = int(input("How many players do you want? (1 or 2)\n"))
    if num_players == 1 or num_players == 2:
        if num_players == 1:
            char_p1 = input("Do you want to use X or O?\n")
            if char_p1 == 'X':
                char_p2 = 'O'
            else:
                char_p2 = 'X'
            return char_p1, char_p2
        else:
            ask_again = True
            while ask_again == True:
                char_p1 = input("Player 1, do you want X or O?\n")
                char_p2 = input("Player 2, do you want X or O?\n")
                if char_p1 == char_p2:
                    print("You cannot pick the same character, please enter again.\n")
                    ask_again = True
                else:
                    ask_again = False
                    return char_p1, char_p2

def play_game(board, char_p1, char_p2):

    row = int(input("Player 1, enter the row you want to choose\n"))
    column = int(input("Enter the column you want to choose\n"))
    board[row][column] = char_p1
    winner = check_winner(board, row, column)
    if winner == True:
        exit
    print_board(board)

    row = int(input("Player 2, enter the row you want to choose\n"))
    column = int(input("Enter the column you want to choose\n"))
    board[row][column] = char_p2
    winner = check_winner(board, row, column)
    if winner == True:
        exit
    print_board(board)

def check_winner(board, i, j):
    for i in range(2):
        for j in range(2):
            if board[0][j] == board[1][j] == board[2][j]:
                return True
            if board[i][0] == board[i][1] == board[i][2]:
                return True
            if i == j and board[0][0] == board[1][1] == board[2][2]:
                return True

            return False
    


def main():
    board = create_board()
    print_board(board)
    char_p1, char_p2 = get_player_info()
    while True:
        play_game(board, char_p1, char_p2)

main()