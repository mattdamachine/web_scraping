from bs4 import BeautifulSoup
import requests

def billboard():
    ''' Grab the top 10 "Billboard Hot 100" songs ''' 
    html_text = requests.get('https://www.billboard.com/charts/hot-100/').text
    soup = BeautifulSoup(html_text, 'lxml')

    items = soup.find_all('div', class_='o-chart-results-list-row-container')[:15]

    for index, item in enumerate(items):
        song = item.find('h3', id='title-of-a-story')

        artist = song.find_next_sibling()


        print(f'Song #{index + 1}: \"{song.text.strip()}\"')
        print(f'Artist: {artist.text.strip()}')
        print()