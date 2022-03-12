# Web Scraping packages

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Data Manipulation packages

import pandas as pd

# Visualization packages

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import numpy as np

webdriver_path = Service("C:/Users/diana/Downloads/chromedriver.exe")
HM_url = 'https://www2.hm.com/de_at/search-results.html?q=Damen+Jeans&department=1&sort=stock&image-size=small&image=stillLife&offset=0&page-size=520'


# Select custom Chrome options
options = webdriver.ChromeOptions()
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.add_argument('--disable-extensions')


# Open the Chrome browser H&M
browser = webdriver.Chrome(service = webdriver_path)
browser.get(HM_url)

# Accept cookies H&M website
cookies_button_HM = browser.find_element(By.ID, 'onetrust-accept-btn-handler')
cookies_button_HM.click()

# Create empty lists H&M
titles_list = []
prices_list = []

# Find item's title and prices
item_titles = browser.find_elements(By.CLASS_NAME, 'item-heading')
item_prices = browser.find_elements(By.CLASS_NAME, 'item-price')

# Loop over the item_titles and item_prices
for title in item_titles:
    titles_list.append(title.text)
for price in item_prices:
    prices_list.append(price.text[0:6])  # In case of a sales price and original price get only the sales price

print(titles_list)
print(prices_list)

# Create a table with the itemes' names and prices
dfH = pd.DataFrame(zip(titles_list, prices_list), columns = ['ItemName', 'Price' ])

print(dfH)

# Remove € from price, convert ',' to '.' and convert price to float
dfH['Price'] = dfH['Price'].str.replace(',', '.').str.replace('€', '').astype(float)
print(dfH)

# Add a column for platform
dfH['Platform'] = 'H&M'
print(dfH)

# Check for missing data in H&M
print(dfH.isnull().sum())

# Create a csv file
dfH.to_csv('PriceComaprisonH&M.csv')

# Read csv file
#df = pd.read_csv('PriceComaprisonH&M.csv')

# Plot the chart H&M
sns.set()
_ = sns.boxplot(x = 'Platform', y = 'Price', data = dfH)
_ = plt.title('Prices of Jeans from the shop H&M')
_ = plt.ylabel('Price (EUR)')
_ = plt.xlabel('E-commerce Platform')
plt.show()
plt.close()

# Histogram H&M
dfH["Price"].plot(kind = 'hist')
# Set title
plt.xlabel('H&M Jeans Prices')
plt.show()


# Open the Chrome browser C&A
browser = webdriver.Chrome(service = webdriver_path)

# List of URls C&A
CA_url = ['https://www.c-and-a.com/at/de/shop/search?q=Damen+Jeans',
          'https://www.c-and-a.com/at/de/shop/search?q=Damen+Jeans&pagenumber=2',
          'https://www.c-and-a.com/at/de/shop/search?q=Damen+Jeans&pagenumber=3',
          'https://www.c-and-a.com/at/de/shop/search?q=Damen+Jeans&pagenumber=4',
          'https://www.c-and-a.com/at/de/shop/search?q=Damen+Jeans&pagenumber=5',
          'https://www.c-and-a.com/at/de/shop/search?q=Damen+Jeans&pagenumber=6',
          'https://www.c-and-a.com/at/de/shop/search?q=Damen+Jeans&pagenumber=7',
          'https://www.c-and-a.com/at/de/shop/search?q=Damen+Jeans&pagenumber=8',
          'https://www.c-and-a.com/at/de/shop/search?q=Damen+Jeans&pagenumber=9',
          'https://www.c-and-a.com/at/de/shop/search?q=Damen+Jeans&pagenumber=10',

          ]

# Select custom Chrome options
options = webdriver.ChromeOptions()
#options.add_argument('--headless')
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.add_argument('--disable-extensions')

# Open the Chrome browser C&A
browser = webdriver.Chrome(service = webdriver_path)


# Create empty lists C&A
titles_list_CA = []
prices_list_CA = []

i = 0

while i < 9:
    browser.get(CA_url[i])
    # Find item's title and prices C&A
    item_titles_CA = browser.find_elements(By.CLASS_NAME, 'product-tile__title')
    item_prices_CA = browser.find_elements(By.CLASS_NAME, 'product-tile__price')
    # Loop over the item_titles and item_prices C&A
    for title in item_titles_CA:
        titles_list_CA.append(title.text)
    for price in item_prices_CA:
        prices_list_CA.append(price.text[0:6])
    i= i + 1

print(titles_list_CA)
print(prices_list_CA)

# Create a table with the iteme's name and prices C&A
dfC = pd.DataFrame(zip(titles_list_CA, prices_list_CA), columns = ['ItemName', 'Price' ])

print(dfC)

# Remove € from price and convert price to float from the C&A data frame
dfC['Price'] = dfC['Price'].str.replace(',', '.').str.replace('€', '').astype(float)
print(dfC)

# Add a column for platform to the C&A data frame
dfC['Platform'] = 'C&A'
print(dfC)

# Check for missing data in C&A
print(dfC.isnull().sum())

# This removes any entry with 'Bluse'(shirt) in its title from the C&A data frame
dfC = dfC[dfC['ItemName'].str.contains('Bluse') == False]
print(dfC)

# This removes any entry with 'Tasche'(bag) in its title from the C&A data frame
dfC = dfC[dfC['ItemName'].str.contains('tasche') == False]
print(dfC)

# This removes any entry with 'Rock'(skirt) in its title from the C&A data frame
dfC = dfC[dfC['ItemName'].str.contains('rock') == False]
print(dfC)

# This removes any entry with 'Shopper'(bag) in its title from the C&A data frame
dfC = dfC[dfC['ItemName'].str.contains('Shopper') == False]
print(dfC)

# This removes any entry with 'Jacke'(jacket) in its title from the C&A data frame
dfC = dfC[dfC['ItemName'].str.contains('jacke') == False]
print(dfC)

# This removes any entry with 'Kleid'(dress) in its title from the C&A data frame
dfC = dfC[dfC['ItemName'].str.contains('kleid') == False]
print(dfC)

# This removes any entry with 'Pullover' in its title from the C&A data frame
dfC = dfC[dfC['ItemName'].str.contains('Pullover') == False]
print(dfC)

# This removes any entry with 'bluse' in its title from the C&A data frame
dfC = dfC[dfC['ItemName'].str.contains('bluse') == False]
print(dfC)

# This removes any entry with 'T-shirt' in its title from the C&A data frame
dfC = dfC[dfC['ItemName'].str.contains('T-Shirt') == False]
print(dfC)


# This removes any entry with 'shirt' in its title from the C&A data frame
dfC = dfC[dfC['ItemName'].str.contains('shirt') == False]
print(dfC)

# Create a csv file from the C&A data frame
dfC.to_csv('PriceComaprisonC&A.csv')

# Read csv file from the C&A data frame
#df = pd.read_csv('PriceComaprisonC&A.csv')

# Plot the chart from the C&A data frame
sns.set()
_ = sns.boxplot(x = 'Platform', y = 'Price', data = dfC)
_ = plt.title('Prices of Jeans from the shop C&A')
_ = plt.ylabel('Price (EUR)')
_ = plt.xlabel('E-commerce Platform')
plt.show()

# Histogram from the C&A data frame
dfC["Price"].plot(kind = 'hist')
# Set title
plt.xlabel('C&A Jeans Prices')
plt.show()

# Concatenate the Dataframes
dfHC = pd.concat([dfH,dfC])

# Create a csv file of the concatenated dataframes
dfHC.to_csv('PriceComaprison_H&M_C&A.csv')
print(dfHC)

# Statistical features of the two platforms H&M and C&A
print(dfHC.groupby(['Platform']).describe())

# Box plot H&M and C&A
sns.set()
_ = sns.boxplot(x = 'Platform', y = 'Price', data = dfHC)
_ = plt.title('Comparison of Jeans prices between H&M and C&A')
_ = plt.ylabel('Price (EUR)')
_ = plt.xlabel('E-commerce Platform')
# Show the plot
plt.show()