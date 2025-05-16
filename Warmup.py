import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin

url = "https://bina.az/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')

items = soup.find_all('div', class_='items-i')

data = []
for item in items:
    title_elem = item.find('div', class_='card_title')
    title = title_elem.text.strip() if title_elem else 'N/A'

    price_elem = item.find('div', class_='price')
    price = price_elem.text.strip() if price_elem else 'N/A'

    location_elem = item.find('div', class_='location')
    location = location_elem.text.strip() if location_elem else 'N/A'

    link_elem = item.find('a', class_='item_link')
    link = urljoin(url, link_elem['href']) if link_elem else 'N/A'

    data.append({
        'Title': title,
        'Price': price,
        'Location': location,
        'Link': link
    })

df = pd.DataFrame(data)

df.to_csv('bina_az_listings.csv', index=False, encoding='utf-8-sig')

print(df)