from OnlineMode.Position import Position


class GameState:
    def __init__(self):
        self.position = Position()
        self.ready = False
        self.winner = None
        self.highlighted_by_active = []
        self.attacked_by_active = None
        self.active_leader = None
        self.active_rolls = []
        self.active_kills = 0

    def set_position(self, position):
        self.position = position

    def set_ready(self, ready):
        self.ready = ready

    def set_winner(self, player_side):
        self.winner = player_side