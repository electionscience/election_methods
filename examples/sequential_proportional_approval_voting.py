import pandas

ballots = [
    {"Red": 1, "Green": 0, "Yellow": 0, "Blue": 1},
    {"Red": 0, "Green": 1, "Yellow": 0, "Blue": 1},
    {"Red": 1, "Green": 0, "Yellow": 1, "Blue": 0},
    {"Red": 1, "Green": 0, "Yellow": 1, "Blue": 1},
    {"Red": 0, "Green": 1, "Yellow": 0, "Blue": 1},
    {"Red": 1, "Green": 0, "Yellow": 1, "Blue": 1},
    {"Red": 1, "Green": 1, "Yellow": 0, "Blue": 1},
    {"Red": 0, "Green": 1, "Yellow": 0, "Blue": 1},
    {"Red": 1, "Green": 0, "Yellow": 0, "Blue": 1},
]

SEATS = 4

seated = []
max_score = max(max(ballot.values()) for ballot in ballots)  # 1 for Approval Voting


def reweight(ballot):
    seated_scores = [ballot[candidate] for candidate in ballot if candidate in seated]
    weight = 1 / (1 + sum(seated_scores) / max_score)
    return {candidate: weight * ballot[candidate] for candidate in ballot}


def nextRound(ballots):
    reweighted_ballots = [reweight(ballot) for ballot in ballots]
    winner = pandas.DataFrame(reweighted_ballots).sum().drop(seated).idxmax()
    print(pandas.DataFrame(reweighted_ballots).sum())
    seated.append(winner)
    return reweighted_ballots


while len(seated) < SEATS:
    nextRound(ballots)
    print(seated)
