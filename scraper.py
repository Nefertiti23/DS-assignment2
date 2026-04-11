# Project 3 | Aqua-Map: Predictive Water Potability Assessment
# Problem Statement: Access to safe drinking water is often compromised by seasonal flooding or
# local contamination. Lab testing is slow and expensive. A predictive model is required to estimate
# water safety based on environmental proxies and historical data.
# Deliverables: An integrated pipeline using UNICEF/WHO data and local weather scrapers, a
# Random Forest classifier for risk levels, and a community alert dashboard.

from bs4 import BeautifulSoup
import requests
import re
# import pandas as pd

html_content = ''
records = []
keywords = {"rainfall", "rains", "rain", "flood", "floods",
    "thunderstorm", "thunderstorms", "landslide", "landslides",
    "hailstorm", "hailstorms", "alert", "alerts"}

try:
    # send a GET request to the URL
    response = requests.get("https://reliefweb.int/report/pakistan/pakistan-rain-monitor-issue-number-1-30-march-08-april-2026")
    html_content = response.content
except Exception as e:
    print("Content retrieval unsuccessful. Error:", e)

soup = BeautifulSoup(html_content, "html.parser")

# print title to check page retrieval
print(soup.title)

# get parent div containing the report content
parent = soup.find("div", class_="rw-report__content")
# get content if parent successfully found
if parent:
    content_div = parent.find("div")
    if content_div:
        # retrieve paragraphs
        paragraphs = content_div.find_all("p")
        # check if paragraph contains keywords
        for p in paragraphs:
            # split paragraph into sentences
            sentences = re.split(r'(?<=[.!?]) +', p.getText())
            for sentence in sentences:
                words = sentence.lower().split()
                if any(word in keywords for word in words):
                    records.append({"text": sentence, "flag": 1})
                else:
                    records.append({"text": sentence, "flag": 0})
else:
    print("Parent not found")

print(records)
# df = pd.DataFrame(records)
# df.to_csv("ndma_events.csv", index=False)
