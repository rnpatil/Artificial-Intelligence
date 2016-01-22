import gamePlay
from copy import deepcopy
from getAllPossibleMoves import getAllPossibleMoves

mycolor=''
def evaluation(board):

    global mycolor
    global Depth
    color=mycolor
    opponentColor = gamePlay.getOpponentColor(color)


    valuekingCorner=0
    value=0
    valueking=0
    valuedefend=0
    finalvalue=0
    defensevalue=0
    valueSideCorner=0
    myXSum=0
    oppXSum=0
    moveAttack=0
    # Loop through all board positions

    for piece in range(1, 33):
        xy = gamePlay.serialToGrid(piece)
        x = xy[0]
        y = xy[1]



        #-------------------------------------------------------------------------------DEFENSE-------------------------------------------------------------------------#
      
        #
        if board[x][y].upper() == color.upper() and piece in (5,12,13,20,21,28):                        # Count my pieces on the side edges and increase the value by one
            valueSideCorner = valueSideCorner + 1
        elif board[x][y].upper() == opponentColor.upper() and piece in (5,12,13,20,21,28):              # Count opponent's pieces on the side edges and decrease the value by one
            valueSideCorner = valueSideCorner - 1
        if board[x][y] == color.upper() and piece in (4,29):                                            # Kings on corners are well defended. Increase the value by 2
            valueSideCorner = valueSideCorner + 2
        elif board[x][y] == opponentColor.upper() and piece in (4,29):                                  # Opponent's Kings on corners are well defended. Decrease the value by 2
            valueSideCorner = valueSideCorner - 2
        if board[x][y].upper() == color.upper()  and color=='r' and piece in (1,2,3,4):                 # Protect my last row of defense .Increase the value by 5 for color==r
            valueSideCorner = valueSideCorner + 5
        elif board[x][y].upper() == color.upper()  and color=='w' and piece in (29,30,31,32):           # Protect my last row of defense .Increase the value by 5 for color==w
            valueSideCorner = valueSideCorner + 5
        elif board[x][y].upper() == opponentColor.upper()  and color=='w' and piece in (29,30,31,32):   # Opponent has last row of defense .Decrease the value by 5 for color==w
            valueSideCorner = valueSideCorner - 5
        elif board[x][y].upper() == opponentColor.upper()  and color=='r' and piece in (1,2,3,4):       # Opponent has last row of defense .Decrease the value by 5 for color==r
            valueSideCorner = valueSideCorner - 5

    defensevalue=valueSideCorner







 # Count how many more pieces I have than the opponent and store it in value
 # Count how many more kings I have than the opponent and store it in valueKing

    for piece in range(1, 33):
        xy = gamePlay.serialToGrid(piece)
        x = xy[0]
        y = xy[1]

        if board[x][y].upper() == color.upper():
            value = value + 1
        elif board[x][y].upper() == opponentColor.upper():
            value = value - 1
        if board[x][y] == color.upper():
            valueking = valueking + 1
        elif board[x][y] == opponentColor.upper():
            valueking = valueking - 1




     # ---------------------------------------------------------------------------------ATTACK----------------------------------------------------------------#

     # Calculate how ahead my pieces are to be promoted as "KINGS" are as compared to opponents pieces.
     #
     # Check if mycolor == r then Add all the x coordinate value of my pieces and store the value in myXSum to see how ahead my pieces are to be promoted
     # In this case the opponentcolor == w, then Add all the (8 minus xcoordinate) value of opponent pieces and store the value in oppXSum to see how ahead opponent pieces are to be promoted
     # Next condition is if mycolor == w then Add all the (8 minus xcoordinate) value of my pieces and store the value in myXSum to see how ahead my pieces are to be promoted
     # Now in this case opponentcolor == r, then Add all the x coordinate value of opponent pieces and store the value in oppXSum to see how ahead opponent pieces are to be promoted


    #  #Calculate Final Attack Value =  ( myXSum minus oppXSum )
    #
    if color== 'r':
      for piece in range(1, 33):
        xy = gamePlay.serialToGrid(piece)
        x = xy[0]
        y = xy[1]
        xopp=8-x
        if board[x][y] == color:
           myXSum=myXSum+x
        elif board[x][y] == opponentColor:
           oppXSum=oppXSum+xopp
    elif color == 'w':
      for piece in range(1, 33):
        xy = gamePlay.serialToGrid(piece)
        x = xy[0]
        y = xy[1]
        xmy=8-x
        if board[x][y] == color:
           myXSum=myXSum+xmy
        elif board[x][y] == opponentColor:
           oppXSum=oppXSum+x


    moveAttack=myXSum-oppXSum


    finalvalue= (value) + (1.4*valueking)  +(2*defensevalue) + moveAttack
    return finalvalue



def nextMove(board, color, time, movesRemaining):
    depth=4
    alpha =float('-inf')
    beta=float('inf')
    global mycolor
    mycolor=color
    moveVal,selectedmove= minimax(board, depth,color,alpha,beta,True)
    return selectedmove

def minimax(board,depth,color,alpha,beta,maximizingPlayer):

    moves = getAllPossibleMoves(board, color)
    evalmove=[]
    opponentColor = gamePlay.getOpponentColor(color)
    if depth == 0 or not moves:                                                     # Terminal Node Condition
        Eval = evaluation(board)
        return  Eval,evalmove

    if maximizingPlayer is True:                                                    # MAX NODE called if maximizingPlayer is True
        bestValue =float('-inf')
        for move in moves:
         if gamePlay.isLegalMove(board, move, color):
          newBoard = deepcopy(board)
          gamePlay.doMove(newBoard,move)
          moveval,moved = minimax(newBoard, depth-1, opponentColor,alpha,beta,False)
          if bestValue == None or moveval > bestValue:
            bestMove = move
            bestValue = moveval
          alpha = max(alpha, moveval)
          if beta <= alpha:
                  break
        return bestValue,bestMove
    else:                                                                          # MIN NODE if maximizingPlayer is False
        bestValue =float('inf')
        for move in moves:
         if gamePlay.isLegalMove(board, move, color):
          newBoard = deepcopy(board)
          gamePlay.doMove(newBoard,move)
          moveval,moved = minimax(newBoard, depth-1, opponentColor,alpha,beta,True)
          if bestValue == None or moveval < bestValue:
            bestMove = move
            bestValue = moveval
          beta = min(beta, moveval)
          if beta <= alpha:
                  break
        return bestValue,bestMove

