import itertools
import pandas as pd

# Compose Ballots
# candidates = ['Squash', 'Potato',  'Broccoli', 'Blueberry', 'Strawberry', 'Banana']
candidates = ["🥕", "🥔", "🥦", "🫐", "🍓", "🍌"]

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
ballots = pd.DataFrame(ballots)
