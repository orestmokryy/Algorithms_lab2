class Hamster:
    def __init__(self, daily_food, greediness):
        self.daily_food = daily_food
        self.greediness = greediness

    def __str__(self):
        return "Daily form = {}, greediness = {}".format(self.daily_food, self.greediness)
