import os

import bs4 as bs
import requests

if __name__ == '__main__':
    URL = '--path to published xml file--'
    img_dir = os.path.join(os.getcwd(), 'img')
    response = requests.get(URL)
    soup = bs.BeautifulSoup(response.text, 'lxml')
    offers = soup.find_all('offer')
    for offer in offers:
        try:
            picture = offer.find('picture')
            xmlid = offer.find('xmlid')
            if xmlid and picture and len(xmlid.text) == 17:
                if picture.text.startswith('http'):
                    response = requests.get(picture.text.strip())
                    with open(os.path.join(img_dir, xmlid.text + '.jpg'), 'wb') as f:
                        f.write(response.content)
        except:
            print('failed to download image ' + xmlid.text if xmlid else '')

