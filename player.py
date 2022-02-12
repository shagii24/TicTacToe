import random
import time
#assign letter to user
class player():
    def __init__(self,letter):
        self.letter=letter

    def move(self,game):
        #check if user inserted numnber
        valid_square = False
        while not valid_square:
            playerMove = input('Please select number: ')
            try:
                playerMove = int(playerMove)
                if game.board[playerMove] != " ":
                    print("this field is already occupied")
                else:
                    valid_square = True
            except:
                #some mechanism to inform user of bad input
                valid_square = False
        print(f'Player {self.letter} moves to filed {playerMove}')
        return playerMove

class human1(player):
    def __init__(self,letter):
        super().__init__(letter)
    def move(self,game):
        return super().move(game)
    
class human2(player):
    def __init__(self,letter):
        super().__init__(letter)
    def move(self,game):
        return super().move(game)

class computerPlayer(player):
    def __init__(self,letter):
        super().__init__(letter)
    def move(self,game):
        computerMove = random.choice([i for i,n in enumerate(game.board) if n == ' '])
        time.sleep(1)
        print(f'Player {self.letter} moves to filed {computerMove}')
        return computerMove