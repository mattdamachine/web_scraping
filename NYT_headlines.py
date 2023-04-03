from bs4 import BeautifulSoup
import requests

def headline():
    ''' Grab the headlines from the NYTimes homepage ''' 
    html_text = requests.get('https://www.nytimes.com').text
    soup = BeautifulSoup(html_text, 'lxml')

    stories = soup.find_all('section', class_='story-wrapper')[:5]

    for story in stories:

        title = story.find('h3')
        if title: 
            title = title.text
        link = story.find('a')
        if link:
            link = link['href']
        summary = story.find('p')
        if summary:
            summary = summary.text

        print(title)
        print(summary)
        print(link)
        print()