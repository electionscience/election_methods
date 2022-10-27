from datetime import date
import pandas as pd
import os


def main():
    # list of files in 'raw' folder
    raw = os.listdir("./raw")
    aggregate = pd.DataFrame()
    for file in raw:
        # read in each file
        df = pd.read_csv(f"./raw/{file}")
        # rename columns
        df["Date"] = file[:4] + "-" + file[4:6] + "-" + file[6:8]
        df["Year"] = file[:4]
        df["State"] = "WA"

        # write to csv
        aggregate = pd.concat([aggregate, df])
    write_to_csv(aggregate)


# rename columns
# "County","Race","Candidate","Party","Votes","PercentageOfTotalVotes","JurisdictionName"


def write_to_csv(df):
    df.to_csv("./washington.csv", index=False)


if __name__ == "__main__":
    main()
