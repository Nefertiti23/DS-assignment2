# Project Name: Detective Fiction Books in Public Domain 
This web scraper will scrape Project Gutenberg's website and produce a dataset of all the books under the detective fiction genre.
### 1. Project Overview
* **Target Website:** 
  * https://www.gutenberg.org/ebooks/bookshelf/30?start_index=
* **Data Fields Extracted:** 
  * Text, Text, Number, Text, Text
  * author, title, total downloads, language, file_type
* **Tools Used:** Python, BeautifulSoup
### 2. Setup Instructions
1. Clone this repo: `https://github.com/Nefertiti23/WebScraping-DS.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Run script: `python scraper.py`
### 3. Challenges & Solutions
* Describe one technical hurdle you overcame (e.g., how you located a specific HTML element or handled
pagination).
* Where available data was textual (eg. '6506 downloads') and required data was integer (eg 6505), separated the digits from textual data and stored them as an integer value in the records.
* From multiple rows in the book details' table, extracyed specific rows only (where `th` = 'language') from a table of variable length for every book by locating the row for which `th` = 'language' and `th` = 'category' were true.
