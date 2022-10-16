import random

class Game:
    def __init__(self, player1, player2, steps):
        self.player1 = player1
        self.player2 = player2
        self.player1_score = 0
        self.player2_score = 0
        if steps == "unknown":
            self.steps = random.randint(1, 20)
        elif steps == "inf":
            self.steps = 1000
        else:
            self.steps = int(steps)

        #0 - silent
        #1 - betray

        self.payout = [[-1, -1], [-3, 0]], [[0, -3], [-2, -2]]


    def play(self):
        for i in range(0, self.steps):
            move1 = self.player1.get_move()
            move2 = self.player2.get_move()

            self.player1.take_info(move2)
            self.player2.take_info(move1)

            self.player1_score += self.payout[move1][move2][0]
            self.player2_score += self.payout[move1][move2][1]

            self.print_move(move1, move2, i)
        print(f"--------------------------------------------------------")


    def print_move(self, move1, move2, tour):
        if move1 == 0:
            move1_str = "Stay silent"
        else:
            move1_str = "Betray"

        if move2 == 0:
            move2_str = "Stay silent"
        else:
            move2_str = "Betray"


        print(f"----------------------Round {tour}----------------------")
        print(f"Player 1 move: {move1_str}, points: {self.player1_score}")
        print(f"Player 2 move: {move2_str}, points: {self.player2_score} ")


