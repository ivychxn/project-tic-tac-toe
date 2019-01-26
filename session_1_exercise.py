import random

def drawBoard(board):
    # This function prints out the board that it was passed and should not return anything
    #HINT: pass a list to this function that holds the position of 'X's and 'O's
    return

def inputPlayerLetter():
    #Ask the player if they want to be 'X' or 'O'
    #Return the chosen letter
    #Hint: Use a loop to keep prompting the player for a letter if the input is not valid

    return

def whoGoesFirst():
    #Randomly choose who goes first
    #Return the string 'computer' or 'player'
    #HINT: look up the documentation for the 'random' library

    return

def main():

    print ('Welcome to Tic Tac Toe')
    starter = whoGoesFirst()

    playerLetter = inputPlayerLetter()
    #Here assign computerLetter to be 'O' if playerLetter is 'X' or vice versa



    #initialize your board list here to pass to draw the board
    #board =
    drawBoard(board)

main()