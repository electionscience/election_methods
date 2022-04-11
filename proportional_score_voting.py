import pandas

ballots = [
  {"Red": 5, "Green": 0, "Yellow": 3, "Blue": 5},
  {"Red": 5, "Green": 0, "Yellow": 0, "Blue": 4},
  {"Red": 0, "Green": 5, "Yellow": 0, "Blue": 1},
  {"Red": 1, "Green": 2, "Yellow": 4, "Blue": 3}, 
  {"Red": 1, "Green": 0, "Yellow": 2, "Blue": 0},  
  {"Red": 1, "Green": 3, "Yellow": 0, "Blue": 1},
  {"Red": 0, "Green": 0, "Yellow": 5, "Blue": 0},
  {"Red": 5, "Green": 0, "Yellow": 0, "Blue": 4},
]

seats = 4
seated = []
max_score = max(max(ballot.values()) for ballot in ballots)

#reweight
def reweight(ballot):
  seated_scores = [
      ballot[candidate] for candidate in ballot if candidate in seated
  ]
  weight = 1/(1+sum(seated_scores)/max_score)
  return {candidate: weight*ballot[candidate] for candidate in ballot}

def nextRound(ballots):
  reweightedBallots = [reweight(ballot) for ballot in ballots] 
  winner = pandas.DataFrame(reweightedBallots).sum().drop(seated).idxmax()
  print(pandas.DataFrame(reweightedBallots).sum())
  seated.append(winner)
  return reweightedBallots

while len(seated) < seats:
  nextRound(ballots)
  print(seated)
