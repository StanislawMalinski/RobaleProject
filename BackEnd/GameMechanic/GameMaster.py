from BackEnd.GameMechanic.GameMechanic import GameMechanic


class GameMaster(GameMechanic):
    def __init__(self):
        super().__init__()
        self.turn = 0
        self.UI = None
        self.display = None

    def newGame(self, player_white, player_black):
        self.BlackPlayer = player_black
        self.WhitePlayer = player_white

    def nextMove(self):
        if self.turn == 0:
            print("Tura białego atak.")
            self.WhitePlayer.performAttack()
            self.updateWindow()
        elif self.turn == 1:
            print("Tura białego ruch.")
            self.WhitePlayer.performMove()
            self.updateWindow()
        elif self.turn == 2:
            print("Tura białego wylęganie.")
            self.WhitePlayer.resources += self.getResourcesForSide("B")
            self.WhitePlayer.performHatchery()
            self.updateWindow()
        elif self.turn == 3:
            print("Tura czarnego atak.")
            self.BlackPlayer.performAttack()
            self.updateWindow()
        elif self.turn == 4:
            print("Tura czarnego ruch.")
            self.BlackPlayer.performMove()
            self.updateWindow()
        elif self.turn == 5:
            print("Tura czarnego wylęganie.")
            self.BlackPlayer.resources += self.getResourcesForSide("C")
            self.BlackPlayer.performHatchery()
            self.turn = -1
            self.updateWindow()
        self.turn += 1
