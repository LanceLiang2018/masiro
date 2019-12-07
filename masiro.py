import requests
from bs4 import BeautifulSoup as Soup


class Masiro:

    HOST = 'https://masiro.moe/'

    def __init__(self):
        pass


    def test(self):
        url = 'https://masiro.moe/forum.php?mod=forumdisplay&fid=241'
        text = requests.get(url).text
        soup = Soup(text, 'html.parser')
        # li = list(soup.find_all(('class', 'threadlisttableid')))
        li = soup.select('table[class=threadlisttableid]')
        print(li)


if __name__ == '__main__':
    m = Masiro()
    m.test()