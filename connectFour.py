import click
import sys
import traceback

blankChar = "▄"
playerOneChar = "x"
playerTwoChar = "o"


def displayBoard(board, boardIndex):
    for line in board:
        print(*line)
    for t in boardIndex:
        print(*t)


def returnFreeSpace(column, board, playerOne):
    origBoard = board
    for i in reversed(board):
        if i[column-1] == blankChar:
            if playerOne:
                i[column-1] = playerOneChar
                return True
            else:
                i[column-1] = playerTwoChar
                return True

    # No changes made if reached here therefore at the top of the board
    return False


def generateBoard(rows, cols):
    board = []
    t = []
    for i in range(rows):
        board.append(t)
        t = []
        for j in range(cols):
            t.append(blankChar)

    boardIndex = []
    eq = []
    nums = []
    for z, i in enumerate(range(cols)):
        eq.append("=")
        nums.append(z)
    print(boardIndex)
    return [board, boardIndex]


def main():
    connectFour = generateBoard(6, 7)
    connectFourBoard = connectFour[0]
    connectFourBoard.remove([])
    connectFourBoardIndex = connectFour[1]

    global x
    x = 0
    while True:
        # click.clear()
        x += 1
        if(x == 2):
            # Player 2
            playerOne = False
            x = 0
        else:
            playerOne = True

        if playerOne:
            def playerOneChoose():
                global x
                click.clear()
                displayBoard(connectFourBoard, connectFourBoardIndex)
                print("\nPlayer One's turn.")
                column = input("What column do you want to drop on? ")

                if(column.isdigit()):
                    pass
                else:
                    playerOneChoose()
                    return
                if ((int(column) <= 7) and (int(column) >= 1)):
                    if returnFreeSpace(int(column), connectFourBoard, playerOne):
                        pass
                    else:
                        x = 0
                else:
                    playerOneChoose()

            playerOneChoose()

        else:
            def playerTwoChoose():
                global x
                click.clear()
                displayBoard(connectFourBoard, connectFourBoardIndex)
                print("\nPlayer Two's turn.")
                column = input("What column do you want to drop on? ")
                if(column.isdigit()):
                    pass

                else:
                    playerTwoChoose()
                    return

                if ((int(column) <= 7) and (int(column) >= 1)):
                    if returnFreeSpace(int(column), connectFourBoard, playerOne):
                        pass

                    else:
                        x = 1

                else:
                    playerTwoChoose()

            playerTwoChoose()


if __name__ == "__main__":
    main()
