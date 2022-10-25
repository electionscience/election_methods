from pandas import pd


def load_data():
    return pd.read_csv("data/raw/wa/wa.csv")


# "County","Race","Candidate","Party","Votes","PercentageOfTotalVotes","JurisdictionName"

# Add year column
df["year"] = 2016

# Add state column
df["state"] = "WA"
