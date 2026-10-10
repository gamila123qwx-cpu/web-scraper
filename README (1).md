# Web Scraper: Books to Excel

A simple Python web scraper that collects book titles and prices from [Books to Scrape](https://books.toscrape.com/) (a website built for scraping practice) and saves them into an Excel file.

## Features

- Downloads the page with `requests`
- Parses the HTML with `BeautifulSoup`
- Extracts each book's title and price
- Converts prices to numbers so they can be sorted and calculated in Excel
- Saves everything to `books.xlsx`
- Opens the Excel file when it finishes (Windows)

## Requirements

- Python 3.x
- Libraries: `requests`, `beautifulsoup4`, `openpyxl`

Install them with:

```bash
python -m pip install requests beautifulsoup4 openpyxl
```

## How to Use

1. Download or clone this repository.
2. Install the libraries (see above).
3. Run the script:

   ```bash
   python scraper.py
   ```

4. The script prints each book to the terminal and creates `books.xlsx` in the same folder.

## Example Output

Terminal:

```
A Light in the Attic - 51.77
Tipping the Velvet - 53.74
Soumission - 50.1
...
Saved books.xlsx
```

Excel file (`books.xlsx`):

| Title                | Price (GBP) |
|----------------------|-------------|
| A Light in the Attic | 51.77       |
| Tipping the Velvet   | 53.74       |
| Soumission           | 50.1        |

## How It Works

1. Sends a request to the website with `requests.get()`.
2. Builds a `BeautifulSoup` object from the page HTML.
3. Finds every book on the page (`article` tags with class `product_pod`).
4. For each book, reads the title from the link and the price from the price tag.
5. Writes each row into an Excel sheet with `openpyxl` and saves the file.

## Important Notes

- The script currently reads all 50 pages(1000 books).
- `os.startfile()` works on Windows only. Remove the last line of the script if you use macOS or Linux.
- Only scrape websites that allow it. Check a site's terms of use and `robots.txt` first. This project uses a practice website made for learning.

## Ideas for Improvement

- Collect more details: rating, availability, and book link
- Handle errors (site down, no internet) without crashing
- Add a short pause between requests to be polite to the server
- Let the user search or filter books by price

## Author

Built by gamila as a python practice project.
