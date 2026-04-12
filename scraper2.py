from bs4 import BeautifulSoup
import requests
# import re
import pandas as pd

html_content = ''
records = []
keywords = {"rainfall", "rains", "rain", "flood", "floods",
    "thunderstorm", "thunderstorms", "landslide", "landslides",
    "hailstorm", "hailstorms", "fog", "foggy", "snowfall", "snowfalls",
    "drought", "smog", "cyclone", "cyclonic", "glof"}

places = {"north", "northern", "upper", "western", "plain",
    "Arabian Sea", "countrywide", "eastern", "indus",
    "chenab", "ravi", "sutlej", "kabul", "GB", "KP", "jhelum",
    "rivers"}

# url will be updated for every page accessed
url = "https://www.ndma.gov.pk/advisories?page="

try:
    for page in range(1, 44):
        # send a GET request to the 43 pages of the NDMA advisory list
        response = requests.get(url + str(page))
        html_content = response.content
        soup = BeautifulSoup(html_content, "html.parser")

        # find all advisory links on the page
        advisory_list = soup.find_all("a", href=True)
        # for every link, extract title and date
        for advisory in advisory_list:
            title = advisory.find("h4")
            date = advisory.find("p")
            if title and date:
                event = None
                place = None
                # extract text from the title
                title_text = title.get_text().lower()
                # split title into words and
                # check if keywords occur in title
                for word in title_text.split():
                    cleaned_word = word.strip('.,!?;:')
                    if cleaned_word in keywords:
                        event = cleaned_word
                        break
                    elif cleaned_word in places:
                        place = cleaned_word
                        break
                # add event and date to records
                records.append({
                    "event": event,
                    "date": date.text.strip(),
                    "place": place
                })

except Exception as e:
    print("Content retrieval unsuccessful. Error:", e)

df = pd.DataFrame(records)
df.to_csv("ndma_advisories.csv", index=True)
