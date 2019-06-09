import requests
from bs4 import BeautifulSoup


def getLinks(url):
    data = requests.get(url)
    soup = BeautifulSoup(data.text, "html.parser")
    data = []
    f = open('links.txt', 'w+')
    for link in soup.find_all(attrs={"class": "spf-link playlist-video clearfix yt-uix-sessionlink spf-link"}, href=True):
        data.append("www.youtube.com"+link['href'])
    for elem in data:
        f.write(elem+"\n")
    f.close()
    return 'links.txt'

