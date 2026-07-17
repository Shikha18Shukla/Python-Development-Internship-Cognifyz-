import csv
import requests
from bs4 import BeautifulSoup

base = "https://books.toscrape.com/catalogue/page-{}.html"

all_books = []

for pg in range(1, 51):
    url = base.format(pg)

    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()

        sp = BeautifulSoup(r.text, "html.parser")

        books = sp.find_all("article", class_="product_pod")

        print(f"Page {pg} -> {len(books)} books")

        for b in books:
            t = b.h3.a["title"]
            p = b.find("p", class_="price_color").text.strip()

            av = (
                b.find("p", class_="instock availability")
                .text.strip()
            )

            rt = b.find("p")["class"][1]

            link = (
                "https://books.toscrape.com/catalogue/"
                + b.h3.a["href"]
            )

            all_books.append([t, p, av, rt, link])

    except Exception as e:
        print(f"Could not scrape page {pg}")
        print(e)

with open("books.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)

    w.writerow([
        "Title",
        "Price",
        "Availability",
        "Rating",
        "Product Link"
    ])

    w.writerows(all_books)

print("-" * 40)
print(f"Total Books : {len(all_books)}")
print("Data saved in books.csv")