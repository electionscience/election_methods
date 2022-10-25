from requests_html import HTMLSession
import re

session = HTMLSession()

# Open https://www.sos.wa.gov/elections/research/election-results-and-voters-pamphlets.aspx
# Get all the dates from the URL paths
# Find all URLs with https://results.vote.wa.gov/results/20211102/ and grab the date from the URL
# Grab f'https://results.vote.wa.gov/results/{date}/export/{date}_AllCounties.csv'

r = session.get(
    "https://www.sos.wa.gov/elections/research/election-results-and-voters-pamphlets.aspx"
)
# print(r.html.links)
pattern = re.compile(r"(?!\/results\/)(\d{8})")
dates = {pattern.search(link)[0] for link in r.html.links if pattern.search(link)}

for date in dates:
    file_url = (
        f"https://results.vote.wa.gov/results/{date}/export/{date}_AllCounties.csv"
    )
    response = session.get(file_url)
    print(f"Writing {file_url}")
    open(f"./{date}.csv", "wb").write(response.content)
