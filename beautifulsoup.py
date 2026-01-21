from bs4 import BeautifulSoup

def extract_data(html):
    soup = BeautifulSoup(html, "html.parser")

    items = soup.find_all("article", class_="product_pod")

    data = []
    for item in items:
        title = item.h3.a["title"]
        price = item.find("p", class_="price_color").text
        data.append((title, price))

    return data
