from bs4 import BeautifulSoup
import pandas as pd
import requests
import time
import re

records = []
url = 'https://www.gutenberg.org/ebooks/bookshelf/30?start_index='

def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup

# extract language and file type from book details page
def extract_details(details_page):
    try:
        details_table = details_page.find('table', class_='bibrec')
        rows = details_table.find_all('tr')
        data = {}

        for row in rows:
            cols = [td.text.strip() for td in row.find_all(['th', 'td'])]
            if cols[0] == 'Language':
                data['language'] = cols[1]
            elif cols[0] == 'Category':
                data['category'] = 'Audiobook' if cols[1] == 'Sound' else 'Ebook'

        return {
            'language': data['language'],
            'file_type': data['category'],
        }

    except Exception as e:
        print("Error extracting details: ", e)
        return {
            'language': 'NA',
            'category': 'NA',
        }

# extract link to the book details
def get_details(book_link):
    details_link = book_link.find('a', class_='link', href=True)

    if details_link:
        details_url = 'https://www.gutenberg.org' + details_link['href']
        details_page = scrape_website(details_url)
        return extract_details(details_page)

    else:
        print("Error loading book details...")

# extract features from list of books
def get_books(page):
    books = []
    try:
        book_links = page.find_all('li', class_='booklink')

        if book_links:
            # loop through all the book links in the current section
            for link in book_links:
                book_name = link.find('span', class_="title")
                book_author = link.find('span', class_="subtitle")
                book_downloads = link.find('span', class_="extra").text
                # convert the downloads text to an integer
                number = re.search(r'\d+', book_downloads)
                if number:
                    book_downloads = int(number.group())

                if book_name and book_author and book_downloads:
                     # store the book details in the records list
                    books.append({
                        'name': book_name.text,
                        'author': book_author.text,
                        'downloads': book_downloads
                    })

                # explore book details for more features
                details = get_details(link)
                if details:
                    books[-1].update(details)

    except Exception as e:
        print("Error loading books: ", e)

    return books

for section in range(0, 6):
    page_content = scrape_website(url + str(25*section))
    time.sleep(1)
    records += get_books(page_content)

df = pd.DataFrame(records)
df.to_csv("public_domain_detective_fiction.csv", index=False)
