# Project Name: Extracting Flood_Event Feature 
This project will result in dataset features, like flooding, which is one of the strongest real-world predictors of water contamination. These can be used for training a predictive model to estimate water safety based on historical data.
### 1. Project Overview
* **Target Websites:** 
  * https://reliefweb.int/country/pak#disasters
* **Data Fields Extracted:** Text, Flag
* **Tools Used:** Python, BeautifulSoup, Pandas
### 2. Setup Instructions
1. Clone this repo: `git clone https://github.com/Nefertiti23/DS-assignment2.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Run script: `python scraper.py`
### 3. Challenges & Solutions
* Describe one technical hurdle you overcame (e.g., how you located a specific HTML element or handled
pagination).
* Located `<p></p>` tags to find text in the page.
* Overcame the possibility of storing entire paragraphs for textual data by splitting paragraphs into sentences and then storing those sentences for documenting.
