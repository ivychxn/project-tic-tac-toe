import random

def draw_board(board):
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("--|---|--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--|---|--")
    print(board[0] + " | " + board[1] + " | " + board[2])
    # This function prints out the board that it was passed and should not return anything
    #HINT: pass a list to this function that holds the position of 'X's and 'O's
    return

def nput_player_letter():
    print("Do you want to be 'X' or 'O' ")
    player_letter = raw_input()
    while(True):
      player_letter = raw_input("Do you want to be 'X' or 'O' ")
      if player_letter == 'X' or player_letter == 'x':
        return player_letter
      if player_letter == 'O' or player_letter == 'o':
        return player_letter
    #Ask the player if they want to be 'X' or 'O'
    #Return the chosen letter
    #Hint: Use a loop to keep prompting the player for a letter if the input is not valid

def who_goes_first():
    if random.randint(0, 1) == 0:
      return "computer"
    #Randomly choose who goes first
    #Return the string 'computer' or 'player'
    #HINT: look up the documentation for the 'random' library

    return "player"

def main():

    print ('Welcome to Tic Tac Toe')
    starter = who_goes_first()

    player_letter = input_player_letter()
    if player_letter == 'X':
    #Here assign computer_letter to be 'O' if player_letter is 'X' or vice versa
      computer_letter = 'O'
    else:
      computer_letter = 'X'


    #initialize your board list here to pass to draw the board
    board = [" "]*9
    draw_board(board)

main()