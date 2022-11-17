# California

Rather than scraping, I just downloaded the files from [the California Elections Data Archive](https://csu-csus.esploro.exlibrisgroup.com/esploro/outputs/dataset/California-Elections-Data-Archive-CEDA/99257830890201671?institution=01CALS_USL)

# CALIFORNIA ELECTIONS DATA ARCHIVE (CEDA)

## CALIFORNIA LOCAL ELECTIONS

## DATA DEFINITIONS AND CODEBOOK

The Secretary of State has given the ISR permission to make available a summary of the results of all local elections for the calendar year, as well as the raw data. ISR collects and tabulates these data for the Secretary of State annually. A hard copy report containing these tables, a summary of results for county, city and school district measures and candidate races, and an analysis of election trends may be ordered from the Secretary of State's office by calling Arman Hirose-Afshari at (916) 695-1602. The file CEDA____Data.xls is an Excel workbook that contains 2 worksheets – one contains all candidate race data and the other contains all data on measures. The table below provides each worksheet name and a description of the data under each column heading. For questions about the data, please contact Valory Messier: vmessier@csus.edu, 916-278-5293. Column headings reporting multi-county data display different data when the relevant political jurisdiction crosses county borders. This occurs only for a small number of county candidate races for superintendent of schools and several school district races; these will be the only instances where the values displayed in these columns will differ from those displayed in their single county equivalents. It is recommended that those interested in school district level data utilize the multi-county variables as opposed to the single county variables when looking at overall results of ballot measures and candidate races. The data files contain a series of unique identifiers that serve different purposes. In the candidate data file, the first variable (`RecordID`) simply provides a row count and should not be used to uniquely identify candidates. There are 2 ID variables that correspond to races. The first ID variable (`RaceID`) identified individual races while assuming that all races are single county. This means that a race for a particular office that crosses county lines will have separate `RaceIDs` for each county. `Multi_RaceID` identifies each race uniquely, even if the race crosses county lines. Similarly, `Multi_CandID` identifies each candidate uniquely. There will only be duplicate `Multi_CandIDs` if the race in which the candidate appears crosses county lines. In the measures data file, `MeasID` identifies each measure assuming all measures are from a single county. `Multi_MeasID` provides unique identifiers for measures that cross county lines. All ID variables contain the corresponding election year as the first 4 digits in order to remain unique in the case that the user combines multiple years of data.

### All County, City and School District Candidate Data (Candidates__.xls worksheet)

| Column             | Heading Data Description                                                                                                                                                                                    |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AREA               | Area within Office – e.g. supervisorial district, school board seat                                                                                                                                         |
| BALDESIG           | Candidate's ballot designation                                                                                                                                                                              |
| CAND#              | Number of candidates running for office                                                                                                                                                                   |
| CHECKRUNOFF        | Confirmed runoff candidates                                                                                                                                                                                 |
| CNTYNAME           | County name                                                                                                                                                                                                 |
| CO                 | Numerical code for county, counties sorted in alphabetical order                                                                                                                                            |
| CSD                | Election for a Community Service District or County Service Area—0=No, 1=Yes                                                                                                                                |
| DATE               | Date of election                                                                                                                                                                                            |
| ELECTED            | Single county outcome for candidate – 1=Elected to office; 2=Not elected to office; 3=Runoff                                                                                                                |
| FIRST              | Candidate's first name                                                                                                                                                                                      |
| INCUMB             | Incumbency status – Y=Incumbent; N=Not incumbent                                                                                                                                                            |
| Indivtotal_votes   | Multi-county votes for candidate                                                                                                                                                                            |
| JUR                | Jurisdiction – 1=County; 2=City; 3=School District                                                                                                                                                          |
| LAST               | Candidate's last name                                                                                                                                                                                       |
| Multi_CandID       | Unique ID identifying candidates across counties (for multi-county races)                                                                                                                                   |
| Multi_CO           | Indicates Multi-County Races – 0 = Single County; 1 = Multi-County                                                                                                                                          |
| Multi_RaceID       | Unique ID identifying races across counties (for multi-county races)                                                                                                                                        |
| Multitotal_votes   | Multi-county total votes all candidates running for office, not including write-ins                                                                                                                         |
| Newelected         | Multi-county outcome for candidate – 1=Elected to office; 2=Not elected to office; 3=Runoff                                                                                                                 |
| Newtotvotes        | Multi-county total votes all candidates running for office, including write-ins                                                                                                                             |
| NUM_INC            | Numeric Incumbency status—1=Yes, 2=No                                                                                                                                                                       |
| OFFICE             | Original office within political jurisdiction                                                                                                                                                               |
| PERCENT            | Percent of total votes received by candidate                                                                                                                                                                |
| PLACE              | Political jurisdiction – name of county, CSD, city or school district                                                                                                                                       |
| RACEID             | Numeric identifier for each contest                                                                                                                                                                         |
| RaceID             | Unique ID for each Race assuming single-county                                                                                                                                                              |
| RECODE_OFFICE      | Numeric categories for office – 1 = County Supervisor; 2 = City Council; 3 = School Board Member ; 4 = CSD/CSA Director; 5 = Other County Office; 6 = Other City Office; 7 = Other School  District Office. |
| RECODE_OFFNAME     | Name for recoded office categories                                                                                                                                                                          |
| RecordID           | Unique ID for each record                                                                                                                                                                                   |
| Rindivto           | Multi-county rank order of candidates for each contest                                                                                                                                                      |
| RUNOFF             | Potential runoff candidates                                                                                                                                                                                 |
| RVOTES             | Rank order of candidates for each contest                                                                                                                                                                   |
| SUMVOTES           | Total votes for all candidates running for office, not including write-ins                                                                                                                                  |
| TERM               | Term of office – full or short                                                                                                                                                                              |
| Totalwritein_votes | Multi-county total write-in votes                                                                                                                                                                           |
| TOTVOTES           | Total votes for all candidates running for office, including write-ins                                                                                                                                      |
| VOTE               | # Number of seats to be filled in office (# of candidates to vote for)                                                                                                                                      |
| VOTES              | Votes for candidate                                                                                                                                                                                         |
| WRITEIN            | Total write-in votes for candidates not listed on ballot                                                                                                                                                    |
| YEAR               | Election Year                                                                                                                                                                                               |

## All County, City and School District Measure Data (Measures__.xls worksheet)

| Column       | Heading Data Description                                                                                                                                                                    |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| MeasID       | Unique identifier for each measure assuming single-county                                                                                                                                   |
| YEAR         | Election Year                                                                                                                                                                               |
| CO           | Numerical code for county, counties sorted in alphabetical order                                                                                                                            |
| JUR          | Jurisdiction – 1=County; 2=City; 3=School District                                                                                                                                          |
| CNTYNAME     | County name                                                                                                                                                                                 |
| DATE         | Date of election                                                                                                                                                                            |
| PLACE        | Political jurisdiction – name of county, CSD, city or school district                                                                                                                       |
| CSD          | Election for a Community Service District or County Service Area—0=No, 1=Yes                                                                                                                |
| MEASTYPE     | Regular measure or recall measure (M=Regular Measure; R=Recall)                                                                                                                             |
| LTR          | Letter or number designation of measure                                                                                                                                                     |
| BALQUEST     | Ballot question text as it appeared on ballot                                                                                                                                               |
| Orig_TYPE    | Original numeric code for measure type, used prior to 1999.                                                                                                                                 |
| RECTYPE      | Numeric code for measure type – see “Measure Type and Topic Codes” (for years 1995- 2012 )                                                                                                  |
| RECTYPENAME  | Name of measure type (for years 1995- 2012 )                                                                                                                                                |
| Orig_TOPIC   | Original numeric code for measure topic, used prior to 1999.                                                                                                                                |
| RECTOPIC     | Numeric code for measure type – see “Measure Type and Topic Codes” (for years 1995- 2012 )                                                                                                  |
| RECTOPNAME   | Name of measure topic (for years 1995- 2012 )                                                                                                                                               |
| YES          | Votes in favor or measure                                                                                                                                                                   |
| NO           | Votes opposed to measure                                                                                                                                                                    |
| TOTAL        | Total votes for measure                                                                                                                                                                     |
| PERCENT      | Percent of votes in favor of measure                                                                                                                                                        |
| REQ          | Required passage for measure – M=Majority; F = Fifty-five; T=Two-thirds                                                                                                                     |
| OUTCOME      | Numeric code for passfail – 1=Pass;2=Fail                                                                                                                                                   |
| PASSFAIL     | Outcome of measure – Pass = Pass Majority REQ; Fail = Fail Majority REQ; PassT = Pass Two-thirds REQ; FailT = Fail Two-thirds REQ; PassF = Pass Fifty-five REQ; FailF = Fail Fifty-five REQ |
| Multi_CO     | Indicates Multi-County Elections – 0 = Single County; 1 = Multi-County                                                                                                                      |
| Multi_MeasID | Unique ID identifying Measures across counties (for multi-county measures)                                                                                                                  |
| YES_sum      | Multi-county votes in favor of measure                                                                                                                                                      |
| NO_sum       | Multi-county votes opposed to measure                                                                                                                                                       |
| Total_sum    | Total multi-county votes for measure                                                                                                                                                        |
| Percent_sum  | Multi-county percent of votes in favor of measure                                                                                                                                           |
| Outcome_sum  | Multi-county numeric code for passfail – 1=Pass;2=Fail                                                                                                                                      |
| Passfail_sum | Multi-county outcome of measure                                                                                                                                                             |
| typerec      | Collapsed numeric code for measure type                                                                                                                                                     |
| topicrec     | Collapsed numeric code for measure topic                                                                                                                                                    |
| OTH          | Ballot choices for measures other than favor or oppose                                                                                                                                      |

# MEASURE TYPE AND TOPIC CODES SUMMARY –CEDA 

## TYPE 

01 Taxes 
02 Business Tax 
03 Property Tax 
04 Sales Tax 
05 Utility Tax 
06 Gasoline Tax
07 Miscellaneous Tax
08 Development Tax
09 Transient Occupancy Tax
10 Bonds 
11 GO Bond 
12 Revenue Bond 
13 Mello/Roos Bond
14 Authorize Expenditure*
20 Charter Amendment
30 Advisory
40 Initiative
50 Recall
60 Gann Limit
70 Ordinance
80 Policy/Position Statement

## TOPIC 
10 Education 
11 Bonds 
12 Districts/Governance 
13 Recalls
14 Special Tax*
15 Curriculum/Policy Issues
20 Land Use 
21 Growth Cap/Boundary 
22 Zoning/Project Approval 
23 Open Space 
24 Private Projects* 
25 Public Projects*
26 Voter Approval Requirement
27 Military Base Conversion
28 Sale/Leasing*
29 Redevelopment
30 Safety 
31 Jails/Courts 
32 Police 
33 Fire 
34 Multiple Emergency Services 
35
36 Emergency Medical/Paramedic
37 Firearms
38 Civil Fines/Criminal Penalties
39 Private Security*
40 Governance 
41 Benefits/Compensation* 
42 Personnel/Labor Relations 
43 Organizational Structure 
44 Formation/Annex./Consol. 
45 Political Reform/Term Limits
46 Recall
47 Contracting/Bidding/Leasing
48 Elections
49 Budget Processes/Expenditures
50 Environment 
51 Parks/Recreation* 
52 Growth Cap* 
53 Agency Creation/Structure
54 Regulation/Mitigation
55 Borrowing/Funding*
60 Transport 
61 Mass Transit 
62 Roads 
63 Traffic Regulation/Reduction
64 Agencies
70 Facilities 
71 Libraries 
72 Health Facilities 
73 Museum/Cultural/Comm Ctrs 
74 Public Works 
75 Zoos
76 Sports Facilities
77 Convention Centers
78 Parks & Recreation
79 Jails/Courts
80 Housing 
81 Affordable
82 Rent Control
90 Gambling
100 General Services 
101 Flood Control/Drainage 
102 Wastewater/Sewage 
103 Solid Waste 
104 Water 
105 Maintenance
106 Social/Welfare
107
108
109 Postal Services*
110 Revenues 
111 Tax Repeal/Reduction/Limit. 
112 Tax Creation/Incr./Contin. 
113 Prop 
114 Voter Approval Requirement
115 Revenue Use*
116 Appropriation Limit Increase*
117 Bond Interest Payment*
200 Other 
201 Revenue Use**
202 Tax Repeal/Reduction/Limit** 
203 Tax Creation/Incr./Contin.** 
204 Noise/Nuisance Abatement* 
205 Promotion of Tourism*
206 Fireworks*
207 Bond Interest Payment**
208 Appropriation Limit Increase**
218 Voter Approval 
* No longer used
**Sub-topic is now part of Revenues
```
