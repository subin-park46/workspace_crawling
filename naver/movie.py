import urllib.request
from bs4 import BeautifulSoup

url = "https://movie.naver.com/movie/running/current.naver"
resp = urllib.request.urlopen(url)
# print(resp)
soup = BeautifulSoup(resp, "html.parser") # resp를 parser해서 html로
# print(soup)
movies = soup.find_all("dl", class_="lst_dsc")
#print(movies)

for movie in movies:
    title = movie.find("a").get_text()
    star = movie.find("span", class_="num").text
    print(f'title : {title} / star : {star}')
