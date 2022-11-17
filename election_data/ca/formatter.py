import os
import logging
import pandas as pd
import sqlite3 as sql
import numpy as np

conn = sql.connect("../elections.db")


# create logger
logger = logging.getLogger("ca_formatter")


def main():
    # list of files in 'raw' folder
    raw = os.listdir("./raw/Candidates")
    aggregate = pd.DataFrame()
    columns = []
    for file in raw:
        # read in each file
        df = pd.read_csv(f"./raw/Candidates/{file}")
        # rename columns
        df = rename_columns(df)
        logger.info(df.columns)
        logger.warning(file)
        logger.info(df[df.index.duplicated()])
        df = df.reindex(sorted(df.columns), axis=1)
        logger.info(df.columns)
        columns.extend(df.columns.tolist())
        df = df.replace("#NULL!", np.nan)
        aggregate = pd.concat([aggregate, df], axis=0, join="outer")
    aggregate = change_types(aggregate)
    aggregate["CNTYNAME"] = aggregate["CNTYNAME"].str.title()
    aggregate["PLACE"] = aggregate["PLACE"].str.title()

    # write to csv
    aggregate.to_sql(
        "candidates",
        conn,
        index=False,
        if_exists="replace",
    )
    logger.info(aggregate.head)


### All County, City and School District Candidate Data (Candidates__.xls worksheet)

# | Column             | Heading Data Description                                                                                                                                                                                    |
# | ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
# | AREA               | Area within Office - e.g. supervisorial district, school board seat                                                                                                                                         |
# | BALDESIG           | Candidate's ballot designation                                                                                                                                                                              |
# | CAND#              | Number of candidates running for office                                                                                                                                                                   |
# | CHECKRUNOFF        | Confirmed runoff candidates                                                                                                                                                                                 |
# | CNTYNAME           | County name                                                                                                                                                                                                 |
# | CO                 | Numerical code for county, counties sorted in alphabetical order                                                                                                                                            |
# | CSD                | Election for a Community Service District or County Service Area—0=No, 1=Yes                                                                                                                                |
# | DATE               | Date of election                                                                                                                                                                                            |
# | ELECTED            | Single county outcome for candidate - 1=Elected to office; 2=Not elected to office; 3=Runoff                                                                                                                |
# | FIRST              | Candidate's first name                                                                                                                                                                                      |
# | INCUMB             | Incumbency status - Y=Incumbent; N=Not incumbent                                                                                                                                                            |
# | Indivtotal_votes   | Multi-county votes for candidate                                                                                                                                                                            |
# | JUR                | Jurisdiction - 1=County; 2=City; 3=School District                                                                                                                                                          |
# | LAST               | Candidate's last name                                                                                                                                                                                       |
# | Multi_CandID       | Unique ID identifying candidates across counties (for multi-county races)                                                                                                                                   |
# | Multi_CO           | Indicates Multi-County Races - 0 = Single County; 1 = Multi-County                                                                                                                                          |
# | Multi_RaceID       | Unique ID identifying races across counties (for multi-county races)                                                                                                                                        |
# | Multitotal_votes   | Multi-county total votes all candidates running for office, not including write-ins                                                                                                                         |
# | Newelected         | Multi-county outcome for candidate - 1=Elected to office; 2=Not elected to office; 3=Runoff                                                                                                                 |
# | Newtotvotes        | Multi-county total votes all candidates running for office, including write-ins                                                                                                                             |
# | NUM_INC            | Numeric Incumbency status—1=Yes, 2=No                                                                                                                                                                       |
# | OFFICE             | Original office within political jurisdiction                                                                                                                                                               |
# | PERCENT            | Percent of total votes received by candidate                                                                                                                                                                |
# | PLACE              | Political jurisdiction - name of county, CSD, city or school district                                                                                                                                       |
# | RACEID             | Numeric identifier for each contest                                                                                                                                                                         |
# | RaceID             | Unique ID for each Race assuming single-county                                                                                                                                                              |
# | RECODE_OFFICE      | Numeric categories for office - 1 = County Supervisor; 2 = City Council; 3 = School Board Member ; 4 = CSD/CSA Director; 5 = Other County Office; 6 = Other City Office; 7 = Other School  District Office. |
# | RECODE_OFFNAME     | Name for recoded office categories                                                                                                                                                                          |
# | RecordID           | Unique ID for each record                                                                                                                                                                                   |
# | Rindivto           | Multi-county rank order of candidates for each contest                                                                                                                                                      |
# | RUNOFF             | Potential runoff candidates                                                                                                                                                                                 |
# | RVOTES             | Rank order of candidates for each contest                                                                                                                                                                   |
# | SUMVOTES           | Total votes for all candidates running for office, not including write-ins                                                                                                                                  |
# | TERM               | Term of office - full or short                                                                                                                                                                              |
# | Totalwritein_votes | Multi-county total write-in votes                                                                                                                                                                           |
# | TOTVOTES           | Total votes for all candidates running for office, including write-ins                                                                                                                                      |
# | VOTE#               | # Number of seats to be filled in office (# of candidates to vote for)                                                                                                                                      |
# | VOTES              | Votes for candidate                                                                                                                                                                                         |
# | WRITEIN     []       | Total write-in votes for candidates not listed on ballot                                                                                                                                                    |
# | YEAR               | Election Year


def rename_columns(df):
    # Add state column
    df["State"] = "CA"
    # df.columns = df.columns.str.upper()
    # if 'RACEID' in df: df = df.drop(['RACEID'])
    df = df.rename(
        columns={
            "checkrunoff": "CHECKRUNOFF",
            "CO#": "CO",
            "Elected": "ELECTED",
            "elected": "ELECTED",
            "First": "FIRST",
            "FIRSTNAME": "FIRST",
            "indivtotal_votes": "Indivtotal_votes",
            "multitotal_votes": "Multitotal_votes",
            "newelected": "Newelected",
            "newtotvotes": "Newtotvotes",
            "last": "LAST",
            "INC": "INCUMB",
            "LASTNAME": "LAST",
            "MeasID": "MeasureID",
            "NUM_INC": "Num_Inc",
            "RACEID": "OtherRaceID",
            "RaceID": "RACEID",
            "Percent": "PERCENT",
            "runoff": "RUNOFF",
            "total_writein": "Totalwritein_votes",
            "Total_writein": "Totalwritein_votes",
            "VOTE#": "SeatsOpen"
            # "RECODE_OFFNAME": ""
            # "VOTES_SUM": "SUMVOTES"
            # RECODE_OFFNAME
        }
    )
    return df


def change_types(df):
    df.Num_Inc = df.Num_Inc.map(dict(Y=1, N=0)).astype("boolean")
    df.INCUMB = df.INCUMB.map(dict(Y=1, N=0)).astype("boolean")
    df.INCUMB = df.INCUMB.map(dict(Y=1, N=0)).astype("boolean")
    df.ELECTED = df.ELECTED.replace(
        {
            1: "ELECTED",
            2: "NOT ELECTED",
            3: "RUNOFF",
            "Yes": "ELECTED",
            "No": "NOT ELECTED",
        }
    )
    # Replace #NULL! with NaN
    df = df.replace("#NULL!", np.nan)
    # df['Indivtotal_votes'] = pd.to_int(df['Indivtotal_votes'], errors='coerce')
    df = df.astype(
        {
            "CSD": "boolean",
            "CHECKRUNOFF": "boolean",
            "Multi_CO": "boolean",
            "Indivtotal_votes": "Int32",
            "Multi_CandID": "Int32",
            "Multi_RaceID": "Int32",
            "Multitotal_votes": "Int32",
            "Newelected": "Int32",
            "Newtotvotes": "Int32",
            "Num_Inc": "Int32",
            "OtherRaceID": "Int32",
            "RECODE_OFFICE": "Int32",
            "RUNOFF": "boolean",
            "RecordID": "Int32",
            "YEAR": "Int32",
            "VOTES_sum": "Int32",
            # "VOTE#": "Int32",
            "SUMVOTES": "Int32",
            "RACEID": "Int32",
        }
    )
    df["TOTVOTES"] = np.floor(pd.to_numeric(df["TOTVOTES"], errors="coerce")).astype(
        "Int64"
    )
    df["WRITEIN"] = np.floor(pd.to_numeric(df["WRITEIN"], errors="coerce")).astype(
        "Int64"
    )
    df["RACEID"] = np.floor(pd.to_numeric(df["RACEID"], errors="coerce")).astype(
        "Int64"
    )

    return df


def reformat_colums(df):
    pass


# todo: pick between INCUMB and NUM_INC
"""
| old                | new                         | Heading Data Description                                                                                                                                                                                   |
| ------------------ | --------------------------- |
| AREA               | district                    | Area within Office - e.g. supervisorial district, school board seat                                                                                                                                        |
| BALDESIG           | ballotdesignation           | Candidate's ballot designation                                                                                                                                                                             |
| CAND#              | number_of_candidates        | Number of candidates running for office                                                                                                                                                                    |
| CHECKRUNOFF        | runoff_candidates           | Confirmed runoff candidates                                                                                                                                                                                |
| CNTYNAME           | county_name                 | County name                                                                                                                                                                                                |
| CO                 | county_number               | Numerical code for county, counties sorted in alphabetical order                                                                                                                                           |
| CSD                | community_service_district? | Election for a Community Service District or County Service Area—0=No, 1=Yes                                                                                                                               |
| DATE               | date                        | Date of election                                                                                                                                                                                           |
| ELECTED            | elected_enum                | Single county outcome for candidate - 1=Elected to office; 2=Not elected to office; 3=Runoff                                                                                                               |
| FIRST              | candidate_first_name        | Candidate's first name                                                                                                                                                                                     |
| INCUMB             | incumbent?                  | Incumbency status - Y=Incumbent; N=Not incumbent                                                                                                                                                           |
| Indivtotal_votes   | multi_county_votes          | Multi-county votes for candidate                                                                                                                                                                           |
| JUR                | jurisdiction_enum           | Jurisdiction - 1=County; 2=City; 3=School District                                                                                                                                                         |
| LAST               | candidate_last_name         | Candidate's last name                                                                                                                                                                                      |
| Multi_CandID       | multi_county_candidate_id   | Unique ID identifying candidates across counties (for multi-county races)                                                                                                                                  |
| Multi_CO           | multi_county_race?          | Indicates Multi-County Races - 0 = Single County; 1 = Multi-County                                                                                                                                         |
| Multi_RaceID       | multi_county_race_id        | Unique ID identifying races across counties (for multi-county races)                                                                                                                                       |
| Multitotal_votes   | multi_county_total_votes    | Multi-county total votes all candidates running for office, not including write-ins                                                                                                                        |
| Newelected         | multi_county_elected_enum   | Multi-county outcome for candidate - 1=Elected to office; 2=Not elected to office; 3=Runoff                                                                                                                |
| Newtotvotes        | multi_county_total_votes    | Multi-county total votes all candidates running for office, including write-ins                                                                                                                            |
| NUM_INC            | incumbent?                  | Numeric Incumbency status—1=Yes, 2=No                                                                                                                                                                      |
| OFFICE             | office                      | Original office within political jurisdiction                                                                                                                                                              |
| PERCENT            | percent_votes               | Percent of total votes received by candidate                                                                                                                                                               |
| PLACE              | race_location               | Political jurisdiction - name of county, CSD, city or school district                                                                                                                                      |
| RACEID             | race_id                     | Numeric identifier for each contest                                                                                                                                                                        |
| RaceID             | year_race_id                | Unique ID for each Race assuming single-county (year+race_id ie, 20110123)                                                                                                                                 |
| RECODE_OFFICE      | office_enum                 | Numeric categories for office - 1 = County Supervisor; 2 = City Council; 3 = School Board Member ; 4 = CSD/CSA Director; 5 = Other County Office; 6 = Other City Office; 7 = Other School District Office. |
| RECODE_OFFNAME     | office_name                 | Name for recoded office categories                                                                                                                                                                         |
| RecordID           | record_id                   | Unique ID for each record                                                                                                                                                                                  |
| Rindivto           | multi_county_rank           | Multi-county rank order of candidates for each contest                                                                                                                                                     |
| RUNOFF             | runoff?                     | Potential runoff candidates                                                                                                                                                                                |
| RVOTES             | rank                        | Rank order of candidates for each contest                                                                                                                                                                  |
| SUMVOTES           | votes_sum                   | Total votes for all candidates running for office, not including write-ins                                                                                                                                 |
| TERM               | full_term?                  | Term of office - full or short                                                                                                                                                                             |
| Totalwritein_votes | multi_county_write_in_votes | Multi-county total write-in votes                                                                                                                                                                          |
| TOTVOTES           | votes_total                 | Total votes for all candidates running for office, including write-ins                                                                                                                                     |
| VOTE#              | pick_x                      | # Number of seats to be filled in office (# of candidates to vote for)                                                                                                                                     |
| VOTES              | votes                       | Votes for candidate                                                                                                                                                                                        |
| WRITEIN            | votes_write_in              | Total write-in votes for candidates not listed on ballot                                                                                                                                                   |
| YEAR               | year                        | Election Year                                                                                                                                                                                              |
"""
if __name__ == "__main__":
    main()
