import os
import logging
import pandas as pd
import sqlite3 as sql
import numpy as np
import sqlalchemy


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
        logger.warning(df[df.index.duplicated()])
        df = df.reindex(sorted(df.columns), axis=1)
        logger.info(df.columns)
        columns.extend(df.columns.tolist())
        df = df.replace("#NULL!", np.nan)
        aggregate = pd.concat([aggregate, df], axis=0, join="outer")
    aggregate = change_types(aggregate)
    # print(aggregate['VOTES'].compare(aggregate['VOTES_sum']).dropna())

    # write to csv
    aggregate.to_csv("./cleaned/CA_candidates.csv", index=False)
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

    """
    | old                | new                         | Type | Heading Data Description                                                                                                                                                                                   |
    | ------------------ | --------------------------- | ---- |----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | AREA               | district                    | String  | Area within Office - e.g. supervisorial district, school board seat                                                                                                                                        |
    | BALDESIG           | ballot_designation           | String  | Candidate's ballot designation                                                                                                                                                                             |
    | CAND#              | number_of_candidates        | Int  | Number of candidates running for office                                                                                                                                                                    |
    | CHECKRUNOFF        | runoff_candidates           | Int  | Confirmed runoff candidates                                                                                                                                                                                |
    | CNTYNAME           | county_name                 | String  | County name                                                                                                                                                                                                |
    | CO                 | county_number               | Int  | Numerical code for county, counties sorted in alphabetical order                                                                                                                                           |
    | CSD                | community_service_district? | boolean  | Election for a Community Service District or County Service Area—0=No, 1=Yes                                                                                                                               |
    | DATE               | date                        | String  | Date of election                                                                                                                                                                                           |
    | ELECTED            | elected_enum                | String  | Single county outcome for candidate - 1=Elected to office; 2=Not elected to office; 3=Runoff                                                                                                               |
    | FIRST              | candidate_first_name        | String  | Candidate's first name                                                                                                                                                                                     |
    | INCUMB             | incumbent?                  | boolean  | Incumbency status - Y=Incumbent; N=Not incumbent                                                                                                                                                           |
    | Indivtotal_votes   | multi_county_votes          | Int  | Multi-county votes for candidate                                                                                                                                                                           |
    | JUR                | jurisdiction_enum           | Int  | Jurisdiction - 1=County; 2=City; 3=School District                                                                                                                                                         |
    | LAST               | candidate_last_name         | String  | Candidate's last name                                                                                                                                                                                      |
    | Multi_CandID       | multi_county_candidate_id   | Int  | Unique ID identifying candidates across counties (for multi-county races)                                                                                                                                  |
    | Multi_CO           | multi_county_race?          | boolean  | Indicates Multi-County Races - 0 = Single County; 1 = Multi-County                                                                                                                                         |
    | Multi_RaceID       | multi_county_race_id        | Int  | Unique ID identifying races across counties (for multi-county races)                                                                                                                                       |
    | Multitotal_votes   | multi_county_total_votes    | Int  | Multi-county total votes all candidates running for office, not including write-ins                                                                                                                        |
    | Newelected         | multi_county_elected_enum   | String  | Multi-county outcome for candidate - 1=Elected to office; 2=Not elected to office; 3=Runoff                                                                                                                |
    | Newtotvotes        | multi_county_total_votes    | Int  | Multi-county total votes all candidates running for office, including write-ins                                                                                                                            |
    | NUM_INC            | incumbent?                  | boolean  | Numeric Incumbency status—1=Yes, 2=No                                                                                                                                                                      |
    | OFFICE             | office                      | Int  | Original office within political jurisdiction                                                                                                                                                              |
    | PERCENT            | percent_votes               | Int  | Percent of total votes received by candidate                                                                                                                                                               |
    | PLACE              | race_location               | Int  | Political jurisdiction - name of county, CSD, city or school district                                                                                                                                      |
    | RACEID             | race_id                     | Int  | Numeric identifier for each contest                                                                                                                                                                        |
    | RaceID             | year_race_id                | Int  | Unique ID for each Race assuming single-county (year+race_id ie, 20110123)                                                                                                                                 |
    | RECODE_OFFICE      | office_enum                 | Int  | Numeric categories for office - 1 = County Supervisor; 2 = City Council; 3 = School Board Member ; 4 = CSD/CSA Director; 5 = Other County Office; 6 = Other City Office; 7 = Other School District Office. |
    | RECODE_OFFNAME     | office_name                 | Int  | Name for recoded office categories                                                                                                                                                                         |
    | RecordID           | record_id                   | Int  | Unique ID for each record                                                                                                                                                                                  |
    | Rindivto           | multi_county_rank           | Int  | Multi-county rank order of candidates for each contest                                                                                                                                                     |
    | RUNOFF             | runoff?                     | boolean  | Potential runoff candidates                                                                                                                                                                                |
    | RVOTES             | rank                        | Int  | Rank order of candidates for each contest                                                                                                                                                                  |
    | SUMVOTES           | votes_sum                   | Int  | Total votes for all candidates running for office, not including write-ins                                                                                                                                 |
    | TERM               | full_term?                  | boolean  | Term of office - full or short                                                                                                                                                                             |
    | Totalwritein_votes | multi_county_write_in_votes | Int  | Multi-county total write-in votes                                                                                                                                                                          |
    | TOTVOTES           | votes_total                 | Int  | Total votes for all candidates running for office, including write-ins                                                                                                                                     |
    | VOTE#              | pick_x                      | Int  | # Number of seats to be filled in office (# of candidates to vote for)                                                                                                                                     |
    | VOTES              | votes                       | Int  | Votes for candidate                                                                                                                                                                                        |
    | WRITEIN            | votes_write_in              | Int  | Total write-in votes for candidates not listed on ballot                                                                                                                                                   |
    | YEAR               | year                        | Int  | Election Year                                                                                                                                                                                              |
    """
    # Add state column
    df["state"] = "CA"
    df = df.rename(
        columns={
            "AREA": "district",
            "BALDESIG": "ballot_designation",
            "CAND#": "number_of_candidates",
            "checkrunoff": "runoff_candidates",
            "CHECKRUNOFF": "runoff_candidates",
            "CNTYNAME": "county_name",
            "CO": "county_number",
            "CO#": "county_number",
            "CSD": "community_service_district?",
            "DATE": "date",
            "ELECTED": "elected_enum",
            "elected": "elected_enum",
            "Elected": "elected_enum",
            "FIRST": "candidate_first_name",
            "First": "candidate_first_name",
            "FIRSTNAME": "candidate_first_name",
            "INC": "incumbent?",
            "INCUMB": "incumbent?",
            "indivtotal_votes": "multi_county_votes",
            "Indivtotal_votes": "multi_county_votes",
            "JUR": "jurisdiction_enum",
            "LAST": "candidate_last_name",
            "last": "candidate_last_name",
            "LASTNAME": "candidate_last_name",
            "Multi_CandID": "multi_county_candidate_id",
            "Multi_CO": "multi_county_race?",
            "Multi_RaceID": "multi_county_race_id",
            "Multitotal_votes": "multi_county_total_votes",
            "multitotal_votes": "multi_county_total_votes",
            "Newelected": "multi_county_elected_enum",
            "newelected": "multi_county_elected_enum",
            "Newtotvotes": "multi_county_total_votes_w_write_in",
            "newtotvotes": "multi_county_total_votes_w_write_in",
            "NUM_INC": "incumbent_enum",
            "Num_Inc": "incumbent_enum",
            "OFFICE": "office",
            "PERCENT": "percent_votes",
            "Percent": "percent_votes",
            "PLACE": "race_location",
            "RACEID": "race_id",
            "RaceID": "year_race_id",
            "RECODE_OFFICE": "office_enum",
            "RECODE_OFFNAME": "office_name",
            "RecordID": "record_id",
            "Rindivto": "multi_county_rank",
            "RUNOFF": "runoff?",
            "runoff": "runoff?",
            "RVOTES": "rank",
            "SUMVOTES": "votes_sum",
            "TERM": "full_term?",
            "total_writein": "multi_county_write_in_votes",
            "Total_writein": "multi_county_write_in_votes",
            "Totalwritein_votes": "multi_county_write_in_votes",
            "TOTVOTES": "votes_total",
            "VOTE#": "pick_x",
            "VOTES_sum": "race_sum_votes",
            "VOTES": "votes",
            "WRITEIN": "votes_write_in",
            "YEAR": "year",
        }
    )

    return df


def change_types(df):
    # Replace #NULL! with NaN
    df["incumbent_enum"] = df["incumbent_enum"].map(dict(Y=1, N=0)).astype("boolean")
    df["incumbent?"] = df["incumbent?"].map(dict(Y=1, N=0)).astype("boolean")
    df["community_service_district?"] = df["community_service_district?"].astype(
        "boolean"
    )
    df["full_term?"] = (
        df["full_term?"].map({"full": True, "short": False}).astype("boolean")
    )
    df.jurisdiction_enum = df.jurisdiction_enum.map(
        {1: "County", 2: "City", 3: "School District"}
    )
    df.multi_county_elected_enum = df.multi_county_elected_enum.replace(
        {
            1: "ELECTED",
            2: "NOT ELECTED",
            3: "RUNOFF",
            "Yes": "ELECTED",
            "No": "NOT ELECTED",
        }
    )
    df.elected_enum = df.elected_enum.replace(
        {
            1: "ELECTED",
            2: "NOT ELECTED",
            3: "RUNOFF",
            "Yes": "ELECTED",
            "No": "NOT ELECTED",
        }
    )
    df = df.replace("#NULL!", np.nan)
    df["votes_total"] = np.floor(
        pd.to_numeric(df["votes_total"], errors="coerce")
    ).astype("Int64")
    df["votes_write_in"] = np.floor(
        pd.to_numeric(df["votes_write_in"], errors="coerce")
    ).astype("Int64")
    df["race_id"] = np.floor(pd.to_numeric(df["race_id"], errors="coerce")).astype(
        "Int64"
    )
    df["multi_county_write_in_votes"] = np.floor(
        pd.to_numeric(df["multi_county_write_in_votes"], errors="coerce")
    ).astype("Int64")
    df = df.astype(
        {
            "ballot_designation": "string",
            "number_of_candidates": "Int64",
            "runoff_candidates": "Int64",
            "county_name": "string",
            "county_number": "Int64",
            "community_service_district?": "boolean",
            "date": "string",
            "elected_enum": "string",
            "candidate_first_name": "string",
            "incumbent?": "boolean",
            "multi_county_votes": "Int64",
            "jurisdiction_enum": "string",
            "candidate_last_name": "string",
            "multi_county_candidate_id": "Int64",
            "multi_county_race?": "boolean",
            "multi_county_race_id": "Int64",
            "multi_county_total_votes": "Int64",
            "multi_county_elected_enum": "string",
            "multi_county_total_votes": "Int64",
            "incumbent?": "boolean",
            "office": "string",
            "percent_votes": "float64",
            "race_location": "string",
            "race_id": "Int64",
            "year_race_id": "Int64",
            "office_enum": "string",
            "office_name": "string",
            "record_id": "Int64",
            "multi_county_rank": "float64",
            "runoff?": "boolean",
            "rank": "float64",
            "votes_sum": "Int64",
            "full_term?": "boolean",
            "multi_county_write_in_votes": "Int64",
            "votes_total": "Int64",
            "pick_x": "Int64",
            "votes": "Int64",
            "votes_write_in": "Int64",
            "year": "Int64",
        },
        errors="raise",
    )
    return df


# todo: pick between INCUMB and NUM_INC

if __name__ == "__main__":
    main()
