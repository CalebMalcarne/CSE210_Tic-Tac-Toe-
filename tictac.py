import os
from colorama import init
from termcolor import colored
init()
board = [[0,0,0],[0,0,0],[0,0,0]]

def checkWin(board):
    def checkStat(check):
        match check:
            case [1,1,1]:
                return 1
            case [2,2,2]:
                return 2
            case _:
                return -1
    def winStat(stat):
        if 1 in stat:
            return 1
        elif 2 in stat:
            return 2
        else:
            return -1   

    stat = [checkStat([board[y][x] for x in range(3)]) for y in range(3)]
    win = winStat(stat)
    if win == -1:
        stat = [checkStat([board[x][y] for x in range(3)]) for y in range(3)]
        win = winStat(stat)
        if win == -1:
            stat = [checkStat([board[x][x] for x in range(3)])]
            win = winStat(stat)
            if win == -1:
                stat = [checkStat([board[2-i][i] for i in range(2,-1,-1)])]
                win = winStat(stat)
    return win
        
def convert(a):
    b = ' '
    if a == 1:
        b = 'X'
    if a == 2:
        b ='O'
    return b

def printChar(a):
    pass
        
def dispBoard():
    chars = [[convert(board[y][x]) for x in range(3)] for y in range(3)]
    print('  1   2   3')
    print('A ' + chars[0][0] +' | '+chars[0][1]+' | '+ chars[0][2] +  '')
    print(' -----------')
    print('B ' + chars[1][0] +' | '+chars[1][1]+' | '+ chars[1][2] +  '')
    print(' -----------')
    print('C ' + chars[2][0] +' | '+chars[2][1]+' | '+ chars[2][2] +  '') 

def getInputX():
    def decode(coords):
        coords = coords.strip()
        if len(coords) != 3:
            os.system('cls')
            main()

        x = int(coords[1]) - 1
        if x >= 3:
            os.system('cls')
            main()
        y = coords[0]
        xo = coords[2]

        match xo:
            case 'x' | 'X':
                xo = 1
            case 'o' | 'O':
                xo = 2
            case _:
                os.system('cls')
                main()


        match y:
            case 'A' | 'a':
                y = 0
            case 'B' | 'b':
                y = 1
            case 'C' | 'c':
                y = 2
            case _:
                os.system('cls')
                main()
 
        board[y][x] = xo

    coords = input('> ')
    decode(coords)

    if checkWin(board) == 1:
        print("[\'X\'s Win")
    elif checkWin(board) == 2:
        print("\'O\'s Win")
    else:
        os.system('cls')
        main()
def main():
    dispBoard()
    getInputX()

main()