import requests
import urllib
from bs4 import BeautifulSoup




def main():
    from urllib.request import Request, urlopen

    url = "https://www.leboncoin.fr/"
    headers = {
        "User-Agent": "Mozilla/5.0",
        'Referer': "https://www.google.com/",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3"
    }

    req = Request(
        url,
        headers=headers)
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage.text, "lxml")




if __name__ == "__main__":
    main()