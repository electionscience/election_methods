

import pandas as pd

df = pd.read_xlsx('2018.xlsx')

# "County"
# "Race"
# "Candidate"
# "Party"
# "Votes"
# "PercentageOfTotalVotes"
# "JurisdictionName"

# Add year column
df['Year'] = 2016

# Add state column
df['State'] = 'CA'

# rename columns
df = df.rename(columns={
    'CNTYNAME': 'County',
    'OFFICE': 'Race',
    'PLACE': 'JurisdictionName',
    'CANDIDATE': 'Candidate',
    'PARTY': 'Party',
    'VOTES': 'Votes',
    'PERCENT': 'PercentageOfTotalVotes'
})

# RecordID
# RACEID
# CO#
# JUR
# CNTYNAME
# YEAR
# DATE
# PLACE
# CSD
# OFFICE
# RECODE_OFFICE
# AREA
# TERM
# VOTE#
# LAST
# FIRST
# BALDESIG
# INC
# NUM_INC
# CAND#
# VOTES
# WRITEIN
# SUMVOTES
# TOTVOTES
# PERCENT
# ELECTED
# RVOTES
# RUNOFF
# CHECKRUNOFF
# Multi_RaceID
# Multi_CandID
# Multi_CO
# Indivtotal_votes
# Multitotal_votes
# Total_writein
# Newtotvotes
# Rindivto
# Newelected