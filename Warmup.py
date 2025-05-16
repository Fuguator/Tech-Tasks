import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

url = "https://tap.az/elanlar/neqliyyat/avtomobiller"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
}

try:
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
except requests.exceptions.HTTPError as e:
    logging.error(f"HTTP Error: {e}")
    exit(1)
except requests.exceptions.RequestException as e:
    logging.error(f"Request failed: {e}")
    exit(1)

soup = BeautifulSoup(response.text, 'html.parser')

items = soup.find_all('div', class_='products-i')

data = []
for item in items:
    try:
        title_elem = item.find('div', class_='products-name')
        title = title_elem.text.strip() if title_elem else 'N/A'

        price_elem = item.find('div', class_='products-price')
        price = price_elem.text.strip() if price_elem else 'N/A'

        location_elem = item.find('div', class_='products-location')
        location = location_elem.text.strip() if location_elem else 'N/A'

        link_elem = item.find('a', class_='products-link')
        link = urljoin(url, link_elem['href']) if link_elem else 'N/A'

        data.append({
            'Title': title,
            'Price': price,
            'Location': location,
            'Link': link
        })
    except Exception as e:
        logging.warning(f"Error processing item: {e}")
        continue

df = pd.DataFrame(data)

if not df.empty:
    df.to_csv('tap_az_cars.csv', index=False, encoding='utf-8-sig')
    logging.info(f"Data saved to tap_az_cars.csv with {len(df)} entries")
else:
    logging.warning("No data was scraped. Check the HTML structure or URL.")

print(df)