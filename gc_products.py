from bs4 import BeautifulSoup
import requests

def new_products():
    ''' Grab the New Products from the Guitar Center home page ''' 
    html_text = requests.get('https://www.guitarcenter.com').text
    soup = BeautifulSoup(html_text, 'lxml')

    # Grab all of the products from the home page
    products = soup.find_all('div', class_='productBlock')

    # Iterate over only the new arrivals
    for product in products[:-24]:

        # product name
        title = product.find('div', class_='prodInfoTitle').text
        # price
        pricing = product.find('div', class_='pricing now').contents[3].text
        # link
        link = product.find('a')['href']

        
        print('Item: ' + title.strip())
        print(pricing.strip())
        print("https://guitarcenter.com" + link)
        print()