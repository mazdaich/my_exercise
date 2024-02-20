class HighScoreTable:
    def __init__(self, n):
        self.max_len = n
        self.scores = []

    def update(self, res):
        self.scores.append(res)
        self.scores = sorted(self.scores, reverse=True)[:self.max_len]

    def reset(self):
        self.scores = []


if __name__ == '__main__':

    high_score_table = HighScoreTable(3)

    print(high_score_table.scores)
    high_score_table.update(10)
    high_score_table.update(8)
    high_score_table.update(12)
    print(high_score_table.scores)

    high_score_table.update(3)
    high_score_table.update(6)
    high_score_table.update(1)
    print(high_score_table.scores)

    high_score_table.reset()
    print(high_score_table.scores)
