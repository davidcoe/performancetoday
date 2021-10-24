from performancetoday.models.episode import Episode


def main():

    import requests
    from bs4 import BeautifulSoup
    import json
    import pprint

    url = 'https://www.yourclassical.org/performance-today'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    Information = soup.find(id='__NEXT_DATA__').string
    y= json.loads(Information)
    #pprint.pprint(y['props']['pageProps']['data']['program']['results']['items'])
    episodes = y['props']['pageProps']['data']['program']['results']['items']
    for episode in episodes:
        title = episode['title']
        publishDate = episode['publishDate']
        description = episode['descriptionText']
        photoUrl = episode['primaryVisuals']['social']['preferredAspectRatio']['instances'][0]['url']
        audioUrl = episode['audio'][0]['encodings'][0]['playFilePath']
        e=Episode(publishDate, title, description, photoUrl, audioUrl)
        print(e)
    pass


if __name__ == '__main__':
    main()
