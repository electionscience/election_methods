# Single Transferrable Vote
import pandas
import numpy

# Ranking a scored ballot because ranked ballots are bad, and annoying to compose.
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
    {"A": 0, "B": 3, "C": 5, "D": 4, "E": 0, "F": 0}

]

seats = 3
ballots = pandas.DataFrame(ballots)
quota = 1+numpy.floor(len(ballots) / (seats + 1))
seated = []

weights = pandas.Series(numpy.ones(len(ballots)), name='weight')


def choices(ballots):
    return pandas.DataFrame(ballots.apply(lambda x: x.idxmax(), axis=1), columns=['choice'])


def summarize(ballots):
    # count highest rated candidate from each row, then count the number of times it occurs
    return pandas.concat([choices(ballots), weights], axis=1).groupby('choice').sum()


def eliminate_zeros(ballots):
    # eliminate candidates who have no first place votes
    eliminated = ballots.columns.difference(summarize(ballots).index)
    if not eliminated.empty: 
        print(f"{eliminated[0] = }, no first place votes")
    return ballots.drop(eliminated, axis=1)


def eliminate_lowest(ballots):
    # if no candidate meets the quota, eliminate the worst performing candidate
    round_count = summarize(ballots)
    if round_count[round_count['weight'] >= quota].empty:
        eliminated = round_count.idxmin().values[0]
        print(f"{eliminated[0] = }, no candidate meets quota, eliminated lowest")
        return ballots.drop(eliminated, axis=1)
    return ballots


def elect_and_distribute_excess(ballots, weights):
    round_count = summarize(ballots)
    # Elect the candidates who have passed the quota
    winner = round_count[round_count['weight'] >= quota].index[0]
    seated.extend(winner)
    excess_votes = round_count.loc[winner].values[0] - quota
    print(f"{seated =}, {quota = }, {excess_votes = }")
    fractional_votes = excess_votes / round_count.max()
    # divide the excess votes by the number of votes for the winner for the value of the excess votes

    # find the second choice votes of those who voted for the winner
    voted_for_winner = choices(ballots)[choices(ballots) == winner].dropna()
    ballots = ballots.drop(winner, axis=1)
    # redistribute the excess votes to the second choices
    weights.iloc[voted_for_winner.index] = fractional_votes
    return ballots, weights


while len(seated) < seats:
    ballots = eliminate_zeros(ballots)
    ballots = eliminate_lowest(ballots)
    ballots, weights = elect_and_distribute_excess(ballots, weights)
