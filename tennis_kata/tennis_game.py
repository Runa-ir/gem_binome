class TennisGame(object):

    def __init__(self):
        self.map_points = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty", 4: "Advantage {}"}
        self.points_player1 = 0
        self.points_player2 = 0

    def get_score(self):
        score_difference = self.points_player1 - self.points_player2
        if self.points_player1 >= 3 and score_difference == 0:
            return "Deuce"
        elif self.points_player1 >= 4 and score_difference == 1:
            return self.map_points.get(self.points_player1).format("player1")
        elif self.points_player2 >= 4 and score_difference == -1:
            return self.map_points.get(self.points_player2).format("player2")
        elif self.points_player1 >= 4 and score_difference > 1:
            return "Win for player1"
        elif self.points_player2 >= 4 and score_difference < -1:
            return "Win for player2"

        return f"{self.map_points.get(self.points_player1)} - {self.map_points.get(self.points_player2)}"

    def won_point(self, player_name):
        if player_name == "player1":
            self.points_player1 += 1
        else:
            self.points_player2 += 1