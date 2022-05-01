import pandas as pd


def SPAV(ballots, k):
    df = pd.DataFrame(ballots)
    seated = []
    while len(seated) < k:
        weight = 1 / (1 + df[seated].sum(axis=1))
        remaining = df.drop(seated, axis=1).mul(weight, axis=0)
        seated.append(remaining.sum().idxmax())
    return seated


if __name__ == "__main__":
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
    print(SPAV(ballots, SEATS))
