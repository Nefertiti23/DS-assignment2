from bs4 import BeautifulSoup
import requests
# import re
import pandas as pd

html_content = ''
records = []
keywords = {"rainfall", "rains", "rain", "flood", "floods",
    "thunderstorm", "thunderstorms", "landslide", "landslides",
    "hailstorm", "hailstorms", "fog", "foggy", "snowfall", "snowfalls",
    "drought", "smog", "cyclone", "cyclonic"}

places = {"north", "northern", "upper", "western", "plain",
    "Arabian Sea", "countrywide", "eastern", "indus",
    "chenab", "ravi", "sutlej", "kabul", "GB", "KP", "jhelum",
    "rivers"}

# url will be updated for every page accessed
url = "https://www.ndma.gov.pk/advisories?page="

try:
    # send a GET request to the 43 pages of the NDMA advisory list
    for page in range(1, 44):
        response = requests.get(url + str(page))
        html_content = response.content
        soup = BeautifulSoup(html_content, "html.parser")

        advisory_list = soup.find_all("a", href=True)
        for advisory in advisory_list:
            title = advisory.find("h4")
            date = advisory.find("p")
            if title and date:
                records.append({
                    "title": title.text.strip(),
                    "date": date.text.strip()
                })

except Exception as e:
    print("Content retrieval unsuccessful. Error:", e)

df = pd.DataFrame(records)
df.to_csv("ndma_advisories.csv", index=True)
