from tennis_kata.player import Player


class TennisGame(object):

    def __init__(self):
        self.map_points = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}
        self.player1 = Player("player1")
        self.player2 = Player("player2")

    def get_score(self):
        if self.player1.get_points() >= 3 and self.player1.compare_points(self.player2) == 0:
            return "Deuce"

        for opponent_case in self.return_all_opponents_cases():
            leader_player = opponent_case[0]
            loser_player = opponent_case[1]

            if leader_player.get_points() >= 4 and leader_player.compare_points(loser_player) == 1:
                return f"Advantage {leader_player.get_name()}"
            if leader_player.get_points() >= 4 and leader_player.compare_points(loser_player) > 1:
                return f"Win for {leader_player.get_name()}"

        return self.handle_regular_points()

    def handle_regular_points(self):
        return f"{self.map_points.get(self.player1.get_points())} - {self.map_points.get(self.player2.get_points())}"

    def won_point(self, player_name):
        if player_name == self.player1.get_name():
            self.player1.set_points(self.player1.get_points() + 1)
        else:
            self.player2.set_points(self.player2.get_points() + 1)

    def return_all_opponents_cases(self):
        return [(self.player1, self.player2), (self.player2, self.player1)]
