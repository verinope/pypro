# Import Libraries
import pandas as pd
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup

# URL
url = 'https://www.optikmelawai.com/frame?category=01&gender=3+5&page=1'

# Opening up connection, grabbing the page
uClient = ureq(url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")

# grabs each product
containers = page_soup.findAll("div",{"class":"pad-box2"})

# Creating dataset
titles = []
brands = []
prices = []
discount_prices = []

# loop each product in page
for container in containers:
    title = container.a["title"]
    titles.append(title)

    brand_container = container.findAll("p",{"class":"jdl-prod"})
    brand = brand_container[0].text
    brands.append(brand)

    price_container = container.findAll("span",{"class":"red-price"})
    price = price_container[0].text
    prices.append(price)

    discount_price_container = container.findAll("span",{"style":"white-space: nowrap;"})
    discount_price = discount_price_container[0].text.strip()
    discount_prices.append(discount_price)

kacamata = pd.DataFrame({
'title': titles,
'brand_name': brands,
'price': prices,
'discount_price': discount_prices,
})

kacamata.to_csv('kacamata.csv')
