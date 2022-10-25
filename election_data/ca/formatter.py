import pandas as pd
import os


def main():
    # list of files in 'raw' folder
    raw = os.listdir("./raw")
    aggregate = pd.DataFrame()
    for file in raw:
        # read in each file
        df = pd.read_excel(f"./raw/{file}")
        # rename columns
        df = rename_columns(df)
        # write to csv
        aggregate = pd.concat([aggregate, df])
    write_to_csv(aggregate)


# rename columns


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


def rename_columns(df):
    # Add state column
    df["State"] = "CA"

    df = df.rename(
        columns={
            "CNTYNAME": "County",
            "OFFICE": "Race",
            "PLACE": "JurisdictionName",
            "CANDIDATE": "Candidate",
            "PARTY": "Party",
            "VOTES": "Votes",
            "PERCENT": "PercentageOfTotalVotes",
        }
    )
    return df


def write_to_csv(df):
    df.to_csv("./california.csv", index=False)


if __name__ == "__main__":
    main()
