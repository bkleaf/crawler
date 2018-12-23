from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.tfreeca22.com/home.php")
bsObject = BeautifulSoup(html, "html.parser")

news = bsObject.find_all("table", {"class" : "new_list"})

titles = bsObject.find_all("td", {"class" : "new_list_title"})

subjects = news.find_all("a")

print(subjects)

for td in titles :
    print(td.text)

print(news)




