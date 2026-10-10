import os
import time
import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"

wb = Workbook()
ws = wb.active
ws.title = "Books"
ws.append(["Title", "Price (GBP)"])

page = 1
total = 0

while True:
    try:
        response = requests.get(BASE_URL.format(page), timeout=10)
    except requests.RequestException as error:
        print("Connection problem:", error)
        break

    if response.status_code != 200:
        break  # no more pages

    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")

    for book in books:
        title = book.h3.a["title"]
        price_text = book.find("p", class_="price_color").text
        price = float("".join(c for c in price_text if c.isdigit() or c == "."))
        ws.append([title, price])
        total += 1

    print(f"Page {page} done ({len(books)} books)")
    page += 1
    time.sleep(0.5)  # short pause to be polite to the server

wb.save("books.xlsx")
print(f"Saved {total} books to books.xlsx")
os.startfile("books.xlsx")