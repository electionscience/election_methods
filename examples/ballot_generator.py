import itertools
import pandas as pd


def generate_approval_ballots():
    # Compose Ballots
    candidates = ["Squash", "Potato", "Broccoli", "Blueberry", "Strawberry", "Banana"]
    # candidates = ["🥕", "🥔", "🥦", "🫐", "🍓", "🍌"]

    ballot1 = {
        candidates[0]: 1,
        candidates[1]: 1,
        candidates[2]: 1,
        candidates[3]: 0,
        candidates[4]: 0,
        candidates[5]: 0,
    }
    ballot2 = {
        candidates[0]: 0,
        candidates[1]: 1,
        candidates[2]: 1,
        candidates[3]: 0,
        candidates[4]: 0,
        candidates[5]: 0,
    }
    ballot3 = {
        candidates[0]: 1,
        candidates[1]: 1,
        candidates[2]: 1,
        candidates[3]: 1,
        candidates[4]: 0,
        candidates[5]: 0,
    }
    ballot4 = {
        candidates[0]: 0,
        candidates[1]: 0,
        candidates[2]: 0,
        candidates[3]: 1,
        candidates[4]: 1,
        candidates[5]: 1,
    }
    ballot5 = {
        candidates[0]: 0,
        candidates[1]: 0,
        candidates[2]: 1,
        candidates[3]: 1,
        candidates[4]: 1,
        candidates[5]: 1,
    }
    ballot6 = {
        candidates[0]: 0,
        candidates[1]: 0,
        candidates[2]: 0,
        candidates[3]: 1,
        candidates[4]: 1,
        candidates[5]: 0,
    }

    ballots = (
        list(itertools.repeat(ballot1, 112))
        + list(itertools.repeat(ballot2, 6))
        + list(itertools.repeat(ballot3, 4))
        + list(itertools.repeat(ballot4, 73))
        + list(itertools.repeat(ballot5, 4))
        + list(itertools.repeat(ballot6, 1))
    )
    ballots = pd.DataFrame(ballots)
    return ballots
