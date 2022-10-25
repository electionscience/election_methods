from pandas import pd


def load_data():
    df = pd.read_csv("data/raw/wa/wa.csv")
    return df


# "County","Race","Candidate","Party","Votes","PercentageOfTotalVotes","JurisdictionName"

# Add year column
df["year"] = 2016

# Add state column
df["state"] = "WA"
