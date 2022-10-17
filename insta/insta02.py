from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup

tag = input("search tags : ")
url = f"https://www.instagram.com/explore/tags/{tag}"

service = Service("./chromedriver.exe") # chromedriver 경로설정
driver = webdriver.Chrome(service=service)

driver.get(url)

sleep(3)

soup = BeautifulSoup(driver.page_source, "html.parser") # 3초 뒤에 driver page source 달라, 그걸로 parser 할 것.
divs = soup.find_all("div", class_="_aagv")
# print(divs)

for img in divs:
    print(img.find('img')['src']) # img에서 src 속성만 뽑음.

driver.close()