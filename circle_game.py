"""
Circle Game by JustJeeCode 9/9/2021
Created this game during class time was super bored
Objective of game get the little circle to as many
apples as possible in 60 seconds!
"""

from random import randint

player = 'O'
apple = '*'
bPiece = 'X'
playerPos = 1
lastPlayerPos = 0
points = 0
applePos = randint(1, 16)
lastApplePos = 0

board = [player, bPiece, bPiece, bPiece,
         bPiece, bPiece, bPiece, bPiece,
         bPiece, bPiece, bPiece, bPiece,
         bPiece, bPiece, bPiece, bPiece]

def display_board():
    print(board[0], board[1], board[2], board[3])
    print(board[4], board[5], board[6], board[7])
    print(board[8], board[9], board[10], board[11])
    print(board[12], board[13], board[14], board[15])

def new_move():
    if playerPos == 1:
        board[0] = player
    elif playerPos == 2:
        board[1] = player
    elif playerPos == 3:
        board[2] = player
    elif playerPos == 4:
        board[3] = player
    elif playerPos == 5:
        board[4] = player
    elif playerPos == 6:
        board[5] = player
    elif playerPos == 7:
        board[6] = player
    elif playerPos == 8:
        board[7] = player
    elif playerPos == 9:
        board[8] = player
    elif playerPos == 10:
        board[9] = player
    elif playerPos == 11:
        board[10] = player
    elif playerPos == 12:
        board[11] = player
    elif playerPos == 13:
        board[12] = player
    elif playerPos == 14:
        board[13] = player
    elif playerPos == 15:
        board[14] = player
    elif playerPos == 16:
        board[15] = player

def rand_apple():
    global applePos
    global points
    global lastApplePos

    if lastApplePos == applePos:
        applePos = randint(1, 16)
        rand_apple()
    else:
        if applePos == playerPos:
            lastApplePos = applePos
            points += 1
            applePos = randint(1, 16)
            rand_apple()
        else:
            if applePos == 1:
                board[0] = apple
            elif applePos == 2:
                board[1] = apple
            elif applePos == 3:
                board[2] = apple
            elif applePos == 4:
                board[3] = apple
            elif applePos == 5:
                board[4] = apple
            elif applePos == 6:
                board[5] = apple
            elif applePos == 7:
                board[6] = apple
            elif applePos == 8:
                board[7] = apple
            elif applePos == 9:
                board[8] = apple
            elif applePos == 10:
                board[9] = apple
            elif applePos == 11:
                board[10] = apple
            elif applePos == 12:
                board[11] = apple
            elif applePos == 13:
                board[12] = apple
            elif applePos == 14:
                board[13] = apple
            elif applePos == 15:
                board[14] = apple
            elif applePos == 16:
                board[15] = apple
        
gameOn = True
lastApplePos = applePos

while gameOn:
    rand_apple()
    display_board()
    print("\nPoints: " + str(points))
    
    keyInput = input("")
    print('\n' * 50)
    board = [bPiece, bPiece, bPiece, bPiece,
            bPiece, bPiece, bPiece, bPiece,
            bPiece, bPiece, bPiece, bPiece,
            bPiece, bPiece, bPiece, bPiece]

    if keyInput == "a":
        if playerPos == 1 or playerPos == 5 or playerPos == 9 or playerPos == 13:
            new_move()
        else:
            playerPos -= 1
            new_move()
    if keyInput == "d":
        if playerPos == 4 or playerPos == 8 or playerPos == 12 or playerPos == 16:
            new_move()
        else:
            playerPos += 1
            new_move()
    if keyInput == "w":
        if playerPos == 1 or playerPos == 2 or playerPos == 3 or playerPos == 4:
            new_move()
        else:
            playerPos -= 4
            new_move()
    if keyInput == "s":
        if playerPos == 13 or playerPos == 14 or playerPos == 15 or playerPos == 16:
            new_move()
        else:
            playerPos += 4
            new_move()
    else:
        new_move()



            
