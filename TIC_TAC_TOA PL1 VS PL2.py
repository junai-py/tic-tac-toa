import os #used to clear screen after every move
import random #used for random selection

def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

        
def displayBoard(board):
    clear()
    print('   |   |' )
    print(' ' +board[7]+ ' | ' +board[8]+ ' | ' +board[9]+ ' ')
    print('   |   |' )
    print('-----------')
    print('   |   |' )
    print(' ' +board[4]+ ' | ' +board[5]+ ' | ' +board[6]+ ' ')
    print('   |   |' )
    print('-----------')
    print('   |   |' )
    print(' ' +board[1]+ ' | ' +board[2]+ ' | ' +board[3]+ ' ')
    print('   |   |' )
    
#TO TEST THE BOARD     
#test_board = ['#','X','O','X','O','X','O','X','O','X']
#displayBoard(test_board)

def playerInput():
    marker=' '
    # using while loops to continually ask until you get a correct answer
    while not(marker=='X' or marker=='O'):
        marker= input('PLAYER 1 DO YOU WANT X OR O :').upper()
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')
    
    
def placeMarker(board,marker,position):
    board[position]=marker


#TO TEST THE BOARD
#test_board = ['#','X','O','X','O','X','O','X','O','X']
#placeMarker(test_board,'$',8)
#displayBoard(test_board)




def winCheck(board,mark):
    return(
    (board[1]==board[2]==board[3]==mark)or
    (board[4]==board[5]==board[6]==mark)or
    (board[7]==board[8]==board[9]==mark)or #for to check the rows
    (board[1]==board[4]==board[7]==mark)or
    (board[2]==board[5]==board[8]==mark)or
    (board[3]==board[6]==board[9]==mark)or #for to check the col
    (board[1]==board[5]==board[9]==mark)or
    (board[7]==board[5]==board[3]==mark))  #for to check the diagnols

#to choose which player goes first
def chooseFirst(): 
    if random.randint(0,1)==0:
        return 'player2'
    else:
        return 'player1'
    
def spaceCheck(board,position):
    return board[position]==' '

def fullBoardCheck(board):
    for i in range(1,10):
        if spaceCheck(board,i):
            return False
    return True
#to choose position to place the marker
def playerChoice(board):
    position=0
    while  position not in [1,2,3,4,5,6,7,8,9] or not spaceCheck(board,position):
        position=int(input(' CHOOSE YOUR POSITION(1-9): '))
    return position

#to play again the game
def replay():
        return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

print('###########################################')
print('    WELCOME TO TIC TAC TOA (PL1 vs PL2)    ')
print('###########################################')


####################################################
             #GAME PLAY LOOP#

    
while True:
    theboard=[' '] * 10 #reset the board
    player1marker,player2marker=playerInput()
    turn=chooseFirst()
    print('--------'+turn+ 'goes first--------')
    
    
    
    playgame=input('ARE YOU READY TO PLAY? THEN HIT YES')
    if playgame.lower()[0]=='y':
        gameON = True
    else:
        gameON = False
        
    while gameON:
        if turn == 'player1':
            displayBoard(theboard)
            position = playerChoice(theboard)
            placeMarker(theboard,player1marker,position)
            
            if winCheck(theboard,player1marker):
                displayBoard(theboard)
                print(' PLAYER1 WON THE GAME')
                gameON = False
            else:
                if fullBoardCheck(theboard):
                    displayBoard(theboard)
                    print(' THIS MATCH IS A DRAW')
                    break
                else:
                    turn='player2'
                    
        else:
            displayBoard(theboard)
            position = playerChoice(theboard)
            placeMarker(theboard,player2marker,position)
            
            if winCheck(theboard,player2marker):
                displayBoard(theboard)
                print(' PLAYER2 WON THE GAME')
                gameON = False
            else:
                if fullBoardCheck(theboard):
                    displayBoard(theboard)
                    print(' THIS MATCH IS A DRAW')
                    break
                else:
                    turn='player1'
                    
                    
    if not replay():
        break
            
    
    
    
    























