class Player(object):

    def __init__(self, player_name):
        self.name = player_name
        self.points = 0

    def get_name(self):
        return self.name

    def get_points(self):
        return self.points

    def set_points(self, points):
        self.points = points

    def compare_points(self, opponent):
        return self.points - opponent.get_points()