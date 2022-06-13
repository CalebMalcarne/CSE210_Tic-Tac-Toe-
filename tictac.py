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
                stat =[[board[y][x] for x in range(3) if board[x][y] == 0] for y in range(3)]
                if 0 not in stat[0] and 0 not in stat[1] and 0 not in stat[2]:
                    win = 3
    return win
        
def convert(a):
    b = ' '
    if a == 1:
        b = 'X'
    if a == 2:
        b ='O'
    return b

def printChar(a):
    if a == 'X':
        return(colored(a, 'blue'))
    elif a == 'O':
        return(colored(a, 'yellow'))
    else:
        return(' ')
                
def dispBoard():
    chars = [[convert(board[y][x]) for x in range(3)] for y in range(3)]
    print('  1   2   3')
    print('A ' + str(printChar(chars[0][0])) +' | '+ str(printChar(chars[0][1]) )+' | '+  str(printChar(chars[0][2])) +  '')
    print(' -----------')
    print('B ' + str(printChar(chars[1][0])) +' | '+ str(printChar(chars[1][1])) +' | '+  str(printChar(chars[1][2])) +  '')
    print(' -----------')
    print('C ' + str(printChar(chars[2][0])) +' | '+ str(printChar(chars[2][1])) +' | '+  str(printChar(chars[2][2])) +  '') 

def getInputX():
    def decode(coords):
        coords = coords.strip()
        coordS = coords.split()

        if len(coords) != 3:
            os.system('cls')
            main()

        if(coords[1] == 'X' or coords[1] == 'O' or coords[1] == 'x' or coords[1] == 'o'):
            x = int(coords[2]) - 1
            if x >= 3:
                os.system('cls')
                main()
            y = coords[0]
            xo = coords[1]
        elif(coords[1] == '1' or coords[1] == '2' or coords[1] == '3'):
            x = int(coords[1]) - 1
            if x >= 3:
                os.system('cls')
                main()
            y = coords[0]
            xo = coords[2]
        else:
            os.system('cls')
            main()


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
        print("\'X\'s Win")
    elif checkWin(board) == 2:
        print("\'O\'s Win")
    elif checkWin(board) == 3:
        print("Tie")
    else:
        os.system('cls')
        main()
def main():
    dispBoard()
    getInputX()

main()