from Zad1.player import Player


class RevengePlayer(Player):

    def __init__(self):
        self.betrayed = False

    def get_move(self):
        if not self.betrayed:
            return 0
        else:
            return True

    def take_info(self, oponent_move):
        if oponent_move == 1:
            self.betrayed = True
