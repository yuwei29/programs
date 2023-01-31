from game_logic import board,game,player
class HCIService:
    def __init__(self):
        self.board = board.init_board()
        self.p_red = player.Player('red')
        self.p_black = player.Player('black')
        #self.peaceCount = 0
        self.winner = None

    # def restart(self):
    #     self.board = board.init_board()
    #     self.p_red = player.Player('red')
    #     self.p_black = player.Player('black')
    #     #self.peaceCount = 0
    #     self.winner = None

    def red_play(self,act):
        if self.winner==None:
            _,self.winner = game.update(act,self.p_red,self.p_black,self.board)
    
    def black_play(self):
        if self.winner==None:
            act = self.p_black.play('random',self.board)
            _,self.winner = game.update(act,self.p_black,self.p_red,self.board)
            return act
        else:
            return [-1,-1,-1,-1]