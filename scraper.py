from selenium import webdriver
import time
import requests

from beautifulsoup import extract_data
from db import get_connection

driver = webdriver.Chrome()
driver.get("https://books.toscrape.com/")
time.sleep(3)

current_url = driver.current_url
driver.quit()

response = requests.get(current_url)
html = response.text

data = extract_data(html)

conn = get_connection()
cur = conn.cursor()

query = "INSERT INTO products (title, price) VALUES (%s, %s)"
cur.executemany(query, data)

conn.commit()
cur.close()
conn.close()

print("✅ Selenium + Requests + BS + PostgreSQL done")
