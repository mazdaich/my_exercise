class HighScoreTable:
    def __init__(self, n):
        self.max_len = n
        self.scores = []

    def update(self, res):
        self.scores.append(res)
        self.scores = sorted(self.scores, reverse=True)[:self.max_len]

    def reset(self):
        self.scores = []

