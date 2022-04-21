import pandas as pd
import numpy as np

def uniform_price(weights, quota):
    """Returns the minimal amount of weight that can be taken uniformly
    from each voter such that the total amount taken is one quota."""
    if sum(weights) < quota:
        return float("inf")

    n = len(weights)
    sorted = weights.sort_values()
    for w in sorted:
        if quota / n < w:
            return quota / n
        quota -= w
        n -= 1
    return sorted[-1]


def MES(ballots, k):
    V = ballots.shape[0]
    quota = V / k
    weights = pd.Series(np.ones(V))

    seated = []
    while len(seated) < k:
        prices = ballots.drop(seated, axis=1).apply(lambda col: uniform_price(weights[col == 1], quota))
        if prices.min() < float("inf"):
            w = prices.idxmin()
        else: #default to largest remainders
            w = ballots.drop(seated, axis=1).mul(weights, axis=0).sum().idxmax()

        weights[ballots[w] == 1] = weights[ballots[w] == 1].subtract(prices[w]).clip(0, 1)
        seated.append(w)
        
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
    ballots = pd.DataFrame(ballots)

    SEATS = 4
    print(MES(ballots, SEATS))
