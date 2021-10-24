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
    pprint.pprint(y)


    #print(Information)
    #Such pretty soup
    #print(soup.prettify())
    pass


if __name__ == '__main__':
    main()
