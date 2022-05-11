import itertools
import pandas as pd


def generate_approval_ballots():
    # Compose Ballots
    # candidates = ["Squash", "Potato", "Broccoli", "Blueberry", "Strawberry", "Banana"]
    candidates = ["A", "B", "C", "X", "Y", "Z"]

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


def generate_score_ballots():
    # Compose Ballots
    candidates = ["Squash", "Potato", "Broccoli", "Blueberry", "Strawberry", "Banana"]
    # candidates = ["🥕", "🥔", "🥦", "🫐", "🍓", "🍌"]

    ballot1 = {
        candidates[0]: 5,
        candidates[1]: 5,
        candidates[2]: 5,
        candidates[3]: 0,
        candidates[4]: 0,
        candidates[5]: 0,
    }
    ballot2 = {
        candidates[0]: 3,
        candidates[1]: 5,
        candidates[2]: 5,
        candidates[3]: 2,
        candidates[4]: 2,
        candidates[5]: 2,
    }
    ballot3 = {
        candidates[0]: 5,
        candidates[1]: 5,
        candidates[2]: 5,
        candidates[3]: 5,
        candidates[4]: 0,
        candidates[5]: 0,
    }
    ballot4 = {
        candidates[0]: 0,
        candidates[1]: 0,
        candidates[2]: 0,
        candidates[3]: 5,
        candidates[4]: 5,
        candidates[5]: 4,
    }
    ballot5 = {
        candidates[0]: 0,
        candidates[1]: 0,
        candidates[2]: 4,
        candidates[3]: 5,
        candidates[4]: 5,
        candidates[5]: 5,
    }
    ballot6 = {
        candidates[0]: 0,
        candidates[1]: 0,
        candidates[2]: 0,
        candidates[3]: 5,
        candidates[4]: 5,
        candidates[5]: 3,
    }

    ballots = (
        list(itertools.repeat(ballot1, 112))
        + list(itertools.repeat(ballot2, 6))
        + list(itertools.repeat(ballot3, 4))
        + list(itertools.repeat(ballot4, 73))
        + list(itertools.repeat(ballot5, 4))
        + list(itertools.repeat(ballot6, 1))
    )
    return pd.DataFrame(ballots)


def generate_ranked_ballots():
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
    return pd.DataFrame(ballots)
