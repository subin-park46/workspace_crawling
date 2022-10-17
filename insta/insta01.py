import requests
from bs4 import BeautifulSoup

tag = input("search tags : ")
url = f"https://www.instagram.com/explore/tags/{tag}"

resp = requests.get(url)
soup = BeautifulSoup(resp.text, "html.parser")
print(soup)
divs = soup.find("div", class_="_aagv")
#print(divs)