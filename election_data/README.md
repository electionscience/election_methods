# Election Data

Consolidated State, Local and Federal election data across the USA

## Election Data

This is the home of the Center for Election Science's universal election dataset.

Election data is stored in .csv format and compiled into a SQLite DB for hosting on Datasette.

To update the Datasette instance on data.electionscience.org, run `datasette publish cloudrun ./elections.db --service=elections --install=datasette-vega` with the appropriate permissions. Contact @fsargent for more information.

## Goals

- A unified dataset for all elections across the USA
- A simple tool to query that data to ask questions such as "all elections where the winners have won with fewer than 50% of the vote"

## Tasks/Tools

- Python
- Pandas
- Datasette
- SQLite

## Scraping

Use Requests library to pull a page and pull the links.
More complex pages might require a scraping library like Scrapy.
Download into a `/[state]/raw/` folder with the election state and year in the file name.

## Munging

What does our standardized format look like?

- Election Date
- Election Year
- State
- Place Name
- Place Type (City/County/Other)
- Office
- Candidate Name
- Votes
- Total Votes in Election
- Percentage of Vote
- Winner?
- Available Seats in Election
- Calculated Quota (1/Seats+1)
- Calculated distance from Quota (Percentage of Vote - Quota)
- Can use Initiatives? (Nice to have)

## Dataset Sources

### Alabama

### Alaska

### Arizona

### Arkansas

### California

[California Elections Data Archive (CEDA)](https://csu-csus.esploro.exlibrisgroup.com/esploro/outputs/dataset/California-Elections-Data-Archive-CEDA/99257830890201671?institution=01CALS_USL)

### Colorado

### Connecticut

### Delaware

### Florida

### Georgia

### Hawaii

### Idaho

### Illinois

### Indiana

### Iowa

### Kansas

### Kentucky

### Louisiana

### Maine

### Maryland

### Massachusetts

### Michigan

### Minnesota

### Mississippi

### Missouri

### Montana

### Nebraska

### Nevada

### New Hampshire

### New Jersey

### New Mexico

### New York

### North Carolina

### North Dakota

### Ohio

### Oklahoma

### Oregon

### Pennsylvania

### Rhode Island

### South Carolina

### South Dakota

### Tennessee

### Texas

[https://data.capitol.texas.gov/topic/elections](https://data.capitol.texas.gov/topic/elections)
[https://data.capitol.texas.gov/dataset/vtds](https://data.capitol.texas.gov/dataset/vtds)
[https://data.capitol.texas.gov/dataset/comprehensive-election-datasets-compressed-format](https://data.capitol.texas.gov/dataset/comprehensive-election-datasets-compressed-format)
Nevermind this only has State Wide elections.

### Utah

[https://voteinfo.utah.gov/historical-election-results/](https://voteinfo.utah.gov/historical-election-results/)

### Vermont

### Virginia

### Washington

Find the year, go to Export Results, select All Counties:

[https://results.vote.wa.gov/results/20211102/export.html](https://results.vote.wa.gov/results/20211102/export.html)

[https://results.vote.wa.gov/results/20211102/export/20211102_AllCounties.csv](https://results.vote.wa.gov/results/20211102/export/20211102_AllCounties.csv)

### West Virginia

### Wisconsin

### Wyoming
