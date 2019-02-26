# --------------Session 2---------------%

import random

# initialize your board list as global list here to pass to draw the board
Board = [' '] * 10


def is_winner(board, letter):
    '''We want this function to see if the letter has won the game.
    This function will be called after every move so the game can detect the new move
    Given the board array and letter, return True if the player has won or False if the player
    has not won
        
    Hint: Detect all possibilities on how to win tic tac toe'''
    # check rows
    if Board[1] == letter:
      if Board[1] == Board[2] and Board[1] == Board[3]:
          return True
    
    if Board[4] == letter:
      if Board[4] == Board[5] and Board[4] == Board[6]:
          return True  
    
    if Board[7] == letter:
      if Board[7] == Board[8] and Board[7] == Board[9]:
          return True

    # check columns
    if Board[1] == letter:
      if Board[1] == Board[4] and Board[1] == Board[7]:
          return True

    if Board[2] == letter:
      if Board[2] == Board[5] and Board[2] == Board[8]:
          return True
    
    if Board[3] == letter:
      if Board[3] == Board[6] and Board[3] == Board[9]:
          return True
    
    # check diagonals
    if Board[1] == letter:
      if Board[1] == Board[5] and Board[1] == Board[9]:
          return True
      
    if Board[3] == letter:
      if Board[3] == Board[5] and Board[3] == Board[7]:
          return True

    return False
    
def is_space_free(board, position):
    '''Return True if the space is free, false if it isn't'''
    if board[position] == ' ':
      return True
    return False


def player_move(board):
    '''Should ask the player where they want to go according to this position chart
                    _7_|_8_|_9_
                    _4_|_5_|_6_
                     1 | 2 | 3
                     (similar to the dialpad)
    Also check if the space is free. If not, prompt the player again
    Returns the integer that represents the position of the player move'''
    move = 0
    while (move not in (1,9)):
      move = int(input('Where do you want to place your move?\n'))
      return move

''' board is the game board, comp is the computer letter, play is the player letter '''
def get_computer_move(board, comp, play):
    move = 0

    # Check if board is full
    if(is_board_full(board)):
        return 0

    # Check if computer is playing first. If so, choose center
    if(is_board_empty(board)):
        return 5

    # Check if computer is one away from winning
    move = one_away_from_win(board, comp)
    if(move != 0):
        return move
    
    # Check if player is one away from winning
    move = one_away_from_win(board, play)
    if(move != 0):
        return move
    
    # Check corners
    if(is_space_free(board, 1)):
        return 1
    if(is_space_free(board, 3)):
        return 3
    if(is_space_free(board, 7)):
        return 7
    if(is_space_free(board, 9)):
        return 9

    # Go to center
    if(is_space_free(board, 5)):
        return 5

    # Random
    while(move == 0):
        move = random.randint(1,9)
        if(is_space_free(board, move)):
            return move;
        else:
            move = 0

def one_away_from_win(board, letter):
    ''' Algorithm to block '''
    streak = 0
    move = 0
    # check rows
    for row in range(1,3):
        streak = 0
        rowStart = 1
        for position in range(rowStart,row+2):
            if board[position] == letter:
                streak += 1
            else:
                move = position
        if(streak == 2):
            print(move)
            if( is_space_free( board, move ) ):
                return move
        rowStart += 3

    # check columns
    for col in range(1,3):
        streak = 0
        position = col
        for count in range(1,3):
            if board[position] == letter:
                streak += 1
            else:
                move = position
            position += 3
        if(streak == 2):
            if( is_space_free( board, move ) ):
                return move

    # check diagonals
    streak = 0
    if board[1] == letter:
        streak += 1
    else:
        move = 1 
    if board[5] == letter:
        streak += 1
    else:
        move = 5
    if board[9] == letter:
        streak += 1
    else:
        move = 9
    if(streak == 2):
        if( is_space_free( board, move ) ):
            return move

    streak = 0
    if board[3] == letter:
        streak += 1
    else:
        move = 3 
    if board[5] == letter:
        streak += 1
    else:
        move = 5
    if board[7] == letter:
        streak += 1
    else:
        move = 7
    if(streak == 2):
        if( is_space_free( board, move ) ):
            return move

    # in the case none of it works
    return 0

def make_move(board, letter, position):
    '''Input the letter onto the board at the specified position'''
    board[position] = letter

def is_board_empty(board):
    ''' Checks if board is empty '''
    for position in range(1, 9):
      if((is_space_free(board, position)) == False ):
        return False
    return True

def is_board_full(board):
    '''We need to check is the board is full to declare a tie

    Hint: you can call other functions in this function'''
    for position in range(1, 9):
      if is_space_free(board, position):
        return False
    return True

def play_again():
    '''Ask the player if they want to play again
    Return True is yes, False if no'''
    answer = ''
    while (answer not in ['YES', 'NO', 'Y', 'N']):
      answer = input('Do you want to play again?\n').upper()
    if answer == 'YES' or answer == 'Y':
      return True
    return False

def clear_board(board):
    for position in range(1, 9):
      board[position] = ' '

# --------------Session 1---------------%
import random


def draw_board(board):
    # This function prints out the board that it was passed and should not return anything
    # HINT: pass a list to this function that holds the position of 'X's and 'O's
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('\n')


def input_player_letter():
    # Ask the player if they want to be 'X' or 'O'
    # Return the chosen letter
    # Hint: Use a loop to keep prompting the player for a letter if the input is not valid
    letter = ''
    while (letter not in ['X', 'O']):
        letter = input('Do you want to be X or O?\n').upper()
    return letter


def who_goes_first():
    # Randomly choose who goes first
    # Return the string 'computer' or 'player'
    # HINT: look up the documentation for the 'random' library
    if random.randint(0, 1) == 0:
        # print('You are going first!')
        return 'player'
    else:
        # print('You are going second!')
        return 'computer'


def main():
    print('Welcome to Tic Tac Toe')  # print beginning message

    # now we will use all of our helper functions to create the workflow of the game
    while True:
        # Reset the board, run the setup functions

        # indicate who will go first
        turn = who_goes_first()
        print('The ' + turn + ' will go first')

        # Ask the player for their letter
        player_letter = input_player_letter()
        if player_letter == 'X':
            computer_letter = 'O'
        else:
            computer_letter = 'X'
        game_on = True

        while (game_on):

            # check if player of computer is the starter, then make their move and check for win or tie
            
            #player_has_made_move = 0

            # have a case for if player goes or if computer will go which will
            # 1. draw the board
            draw_board(Board)
            
            move = 0
            CMove = 0

            
            # 2 & 3 get the move from respective player
            while( move == 0 ):
                move = player_move(Board)
                if(is_space_free(Board, move) == True):
                    make_move(Board, player_letter, move)
                    #player_has_made_move = 1
                else:
                    move = 0
            draw_board(Board)

            while( CMove == 0 ):
                CMove = get_computer_move(Board, computer_letter, player_letter)
                print(CMove)
                if( is_space_free(Board, CMove) == True):
                    make_move(Board, computer_letter, CMove)
                else:
                    CMove = 0

            # 4. check if player/computer won
            track = 0
            if is_winner(Board, player_letter):
              print('Player won bruh')
              draw_board(Board)
              if play_again() == True:
                clear_board(Board)
              else:
                game_on = False

            if is_winner(Board, computer_letter):
              print('Computer won bruh')
              draw_board(Board)
              if play_again() == True:
                clear_board(Board)
              else:
                game_on = False
            
            # 5. check if its is a tie
            if is_board_full(Board):
              "issa tie"
              if play_again() == True:
                clear_board(Board)
              else:
                game_on = False

        
        exit()
            # when the game ends (game_on = False), ask if the player will want to play again
            # break if they do not want to play again
            



main()
