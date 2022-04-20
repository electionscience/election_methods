import numpy as np
import pandas as pd


def STV(ballots, seats, quota):
    V, C = ballots.shape

    weights = np.ones(V)
    elected = []
    remaining = list(ballots.columns)

    for _ in range(seats):
        y = ballots.max(axis=1)
        y = pd.concat([y] * len(remaining), axis=1).rename(
            columns=lambda i: ballots.columns[i]
        )
        fp = y == ballots
        support = fp.mul(weights, axis=0).sum(axis=0)

        while support.max() < quota and len(remaining) > seats - len(elected):
            remaining.remove(support.idxmin())
            ballots = ballots[remaining]

            y = ballots.max(axis=1)
            y = pd.concat([y] * len(remaining), axis=1).rename(
                columns=lambda i: ballots.columns[i]
            )
            fp = y == ballots
            support = fp.mul(weights, axis=0).sum(axis=0)

        winner = support.idxmax()
        surplus = max(1, support.max() / quota)
        weights[fp[winner]] *= 1 - 1 / surplus

        elected.append(winner)
        remaining.remove(winner)
        ballots = ballots[remaining]

    return elected


if __name__ == "__main__":
    ballots = [
        {"A": 5, "B": 4, "C": 3, "D": 0, "E": 0, "F": 0},
        {"A": 5, "B": 4, "C": 3, "D": 0, "E": 0, "F": 0},
        {"A": 5, "B": 4, "C": 3, "D": 0, "E": 0, "F": 0},
        {"A": 5, "B": 4, "C": 3, "D": 0, "E": 0, "F": 0},
        {"A": 5, "B": 4, "C": 3, "D": 0, "E": 0, "F": 0},
        {"A": 5, "B": 4, "C": 3, "D": 0, "E": 0, "F": 0},
        {"A": 5, "B": 4, "C": 3, "D": 0, "E": 0, "F": 0},
        {"A": 5, "B": 4, "C": 3, "D": 0, "E": 0, "F": 0},
        {"A": 5, "B": 4, "C": 3, "D": 0, "E": 0, "F": 0},
        {"A": 5, "B": 4, "C": 3, "D": 0, "E": 0, "F": 0},
        {"A": 5, "B": 4, "C": 3, "D": 0, "E": 0, "F": 0},
        {"A": 5, "B": 4, "C": 3, "D": 0, "E": 0, "F": 0},
        {"A": 5, "B": 4, "C": 3, "D": 0, "E": 0, "F": 0},
        {"A": 5, "B": 4, "C": 3, "D": 0, "E": 0, "F": 0},
        {"A": 5, "B": 4, "C": 3, "D": 0, "E": 0, "F": 0},
        {"A": 5, "B": 4, "C": 3, "D": 0, "E": 0, "F": 0},
        {"A": 5, "B": 4, "C": 3, "D": 0, "E": 0, "F": 0},
        {"A": 5, "B": 4, "C": 3, "D": 0, "E": 0, "F": 0},
        {"A": 5, "B": 4, "C": 3, "D": 0, "E": 0, "F": 0},
        {"A": 5, "B": 4, "C": 3, "D": 0, "E": 0, "F": 0},
        {"A": 0, "B": 5, "C": 0, "D": 4, "E": 2, "F": 1},
        {"A": 0, "B": 5, "C": 0, "D": 4, "E": 2, "F": 1},
        {"A": 0, "B": 5, "C": 0, "D": 4, "E": 2, "F": 1},
        {"A": 0, "B": 5, "C": 0, "D": 4, "E": 2, "F": 1},
        {"A": 0, "B": 5, "C": 0, "D": 4, "E": 2, "F": 1},
        {"A": 0, "B": 5, "C": 0, "D": 4, "E": 2, "F": 1},
        {"A": 0, "B": 5, "C": 0, "D": 4, "E": 2, "F": 1},
        {"A": 0, "B": 5, "C": 0, "D": 4, "E": 2, "F": 1},
        {"A": 0, "B": 5, "C": 0, "D": 4, "E": 2, "F": 1},
        {"A": 0, "B": 5, "C": 0, "D": 4, "E": 2, "F": 1},
        {"A": 0, "B": 5, "C": 0, "D": 4, "E": 2, "F": 1},
        {"A": 0, "B": 5, "C": 0, "D": 4, "E": 2, "F": 1},
        {"A": 0, "B": 5, "C": 0, "D": 4, "E": 2, "F": 1},
        {"A": 0, "B": 5, "C": 0, "D": 4, "E": 2, "F": 1},
        {"A": 0, "B": 5, "C": 0, "D": 4, "E": 2, "F": 1},
        {"A": 0, "B": 5, "C": 0, "D": 4, "E": 2, "F": 1},
        {"A": 0, "B": 5, "C": 0, "D": 4, "E": 2, "F": 1},
        {"A": 0, "B": 5, "C": 0, "D": 4, "E": 2, "F": 1},
        {"A": 0, "B": 5, "C": 0, "D": 4, "E": 2, "F": 1},
        {"A": 0, "B": 5, "C": 0, "D": 4, "E": 2, "F": 1},
        {"A": 4, "B": 0, "C": 1, "D": 0, "E": 0, "F": 5},
        {"A": 4, "B": 0, "C": 1, "D": 0, "E": 0, "F": 5},
        {"A": 4, "B": 0, "C": 1, "D": 0, "E": 0, "F": 5},
        {"A": 4, "B": 0, "C": 1, "D": 0, "E": 0, "F": 5},
        {"A": 4, "B": 0, "C": 1, "D": 0, "E": 0, "F": 5},
        {"A": 4, "B": 0, "C": 1, "D": 0, "E": 0, "F": 5},
        {"A": 4, "B": 0, "C": 1, "D": 0, "E": 0, "F": 5},
        {"A": 4, "B": 0, "C": 1, "D": 0, "E": 0, "F": 5},
        {"A": 4, "B": 0, "C": 1, "D": 0, "E": 0, "F": 5},
        {"A": 4, "B": 0, "C": 1, "D": 0, "E": 0, "F": 5},
        {"A": 4, "B": 0, "C": 1, "D": 0, "E": 0, "F": 5},
        {"A": 4, "B": 0, "C": 1, "D": 0, "E": 0, "F": 5},
        {"A": 4, "B": 0, "C": 1, "D": 0, "E": 0, "F": 5},
        {"A": 4, "B": 0, "C": 1, "D": 0, "E": 0, "F": 5},
        {"A": 4, "B": 0, "C": 1, "D": 0, "E": 0, "F": 5},
        {"A": 4, "B": 0, "C": 1, "D": 0, "E": 0, "F": 5},
        {"A": 4, "B": 0, "C": 1, "D": 0, "E": 0, "F": 5},
        {"A": 4, "B": 0, "C": 1, "D": 0, "E": 0, "F": 5},
        {"A": 4, "B": 0, "C": 1, "D": 0, "E": 0, "F": 5},
        {"A": 4, "B": 0, "C": 1, "D": 0, "E": 0, "F": 5},
        {"A": 0, "B": 0, "C": 4, "D": 5, "E": 3, "F": 2},
        {"A": 0, "B": 0, "C": 4, "D": 5, "E": 3, "F": 2},
        {"A": 0, "B": 0, "C": 4, "D": 5, "E": 3, "F": 2},
        {"A": 0, "B": 0, "C": 4, "D": 5, "E": 3, "F": 2},
        {"A": 0, "B": 0, "C": 4, "D": 5, "E": 3, "F": 2},
        {"A": 0, "B": 0, "C": 4, "D": 5, "E": 3, "F": 2},
        {"A": 0, "B": 0, "C": 4, "D": 5, "E": 3, "F": 2},
        {"A": 0, "B": 0, "C": 4, "D": 5, "E": 3, "F": 2},
        {"A": 0, "B": 0, "C": 4, "D": 5, "E": 3, "F": 2},
        {"A": 0, "B": 0, "C": 4, "D": 5, "E": 3, "F": 2},
        {"A": 0, "B": 0, "C": 4, "D": 5, "E": 3, "F": 2},
        {"A": 0, "B": 0, "C": 4, "D": 5, "E": 3, "F": 2},
        {"A": 0, "B": 0, "C": 4, "D": 5, "E": 3, "F": 2},
        {"A": 0, "B": 0, "C": 4, "D": 5, "E": 3, "F": 2},
        {"A": 0, "B": 0, "C": 4, "D": 5, "E": 3, "F": 2},
        {"A": 0, "B": 0, "C": 4, "D": 5, "E": 3, "F": 2},
        {"A": 0, "B": 0, "C": 4, "D": 5, "E": 3, "F": 2},
        {"A": 0, "B": 0, "C": 4, "D": 5, "E": 3, "F": 2},
        {"A": 0, "B": 0, "C": 4, "D": 5, "E": 3, "F": 2},
        {"A": 0, "B": 0, "C": 4, "D": 5, "E": 3, "F": 2},
        {"A": 0, "B": 3, "C": 5, "D": 4, "E": 0, "F": 0},
        {"A": 0, "B": 3, "C": 5, "D": 4, "E": 0, "F": 0},
        {"A": 0, "B": 3, "C": 5, "D": 4, "E": 0, "F": 0},
        {"A": 0, "B": 3, "C": 5, "D": 4, "E": 0, "F": 0},
        {"A": 0, "B": 3, "C": 5, "D": 4, "E": 0, "F": 0},
        {"A": 0, "B": 3, "C": 5, "D": 4, "E": 0, "F": 0},
        {"A": 0, "B": 3, "C": 5, "D": 4, "E": 0, "F": 0},
        {"A": 0, "B": 3, "C": 5, "D": 4, "E": 0, "F": 0},
        {"A": 0, "B": 3, "C": 5, "D": 4, "E": 0, "F": 0},
        {"A": 0, "B": 3, "C": 5, "D": 4, "E": 0, "F": 0},
        {"A": 0, "B": 3, "C": 5, "D": 4, "E": 0, "F": 0},
        {"A": 0, "B": 3, "C": 5, "D": 4, "E": 0, "F": 0},
        {"A": 0, "B": 3, "C": 5, "D": 4, "E": 0, "F": 0},
        {"A": 0, "B": 3, "C": 5, "D": 4, "E": 0, "F": 0},
        {"A": 0, "B": 3, "C": 5, "D": 4, "E": 0, "F": 0},
        {"A": 0, "B": 3, "C": 5, "D": 4, "E": 0, "F": 0},
        {"A": 0, "B": 3, "C": 5, "D": 4, "E": 0, "F": 0},
        {"A": 0, "B": 3, "C": 5, "D": 4, "E": 0, "F": 0},
        {"A": 0, "B": 3, "C": 5, "D": 4, "E": 0, "F": 0},
    ]

    seats = 3
    ballots = pd.DataFrame(ballots)
    quota = 1 + np.floor(len(ballots) / (seats + 1))

    print(STV(ballots, seats, quota))
