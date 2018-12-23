from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.tfreeca22.com/home.php")
bsObject = BeautifulSoup(html, "html.parser")

print(bsObject)