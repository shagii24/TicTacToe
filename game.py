# print the board 
from player import computerPlayer, human1,human2
import math


class tickTackToe():
    #create empty list to hold results
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner=None

    @staticmethod
    def printNumBoard():
        numBoard = [[str(i) for i in range(j*3,(j+1)*3)] for j in range(3)]
        for i,n in enumerate(numBoard):
            print('| ' + ' | '.join(n) + ' |')
    #print to the user board that contains all moves that were already done

    def printBoard(self):
        for i,n in enumerate([self.board[j*3:(j+1)*3] for j in range(3)]):
            print('| ' + ' | '.join(n) + ' |')

    def emptySquares(self):
        return ' ' in self.board

    def winner(self,square,letter):
        #check if winner in rows
        row_indicator = math.floor(square/3)
        #check row that square is in
        rowCheck = [True if i == letter else False for i in self.board[row_indicator*3:(row_indicator*3)+3]]
        if all(rowCheck):
            return True
        #check columns
        column_indicator=square%3
        #collect squares from column
        col = [n for i,n in enumerate(self.board) if i%3 == column_indicator]
        columnCheck = [True if i == letter else False for i in col]
        if all(columnCheck):
            return True
        if square in [0,4,8]:
            diagon1=[self.board[j] for j in [0,4,8]]
            diagon1Check= [True if i == letter else False for i in diagon1]
            if all(diagon1Check):
                return True
        if square in [2,4,6]:
            diagon2=[self.board[j] for j in [2,4,6]]
            diagon2Check= [True if i == letter else False for i in diagon2]
            if all(diagon2Check):
                return True

def play(game,player1,player2):
    letter = 'X'
    game.printNumBoard()
    while game.emptySquares():
                #how to jump between players
        if letter == 'X':
            gameMove = player1.move(game)
        if letter == 'O':
            gameMove = player2.move(game)
    
        
        myGame.board[gameMove]= letter
        myGame.printBoard()
        if game.winner(gameMove,letter):
            print(f'{letter} won!')
            game.current_winner = letter
            break
        letter = 'O' if letter =='X' else 'X'
    if game.current_winner is None:
        print('Its a tie')

if __name__ == '__main__':

    x_player = human1('X')
    y_player = computerPlayer('O')
    myGame = tickTackToe()
    play(myGame,x_player,y_player)
