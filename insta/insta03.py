from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

input_id = input('id 입력 : ')
input_pw = input('pw 입력 : ')

service = Service('./chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get("https://www.instagram.com/")

sleep(3)
id = driver.find_element(By.NAME, "username") # 이름이 username인 객체 하나 가져오기.
id.send_keys(input_id)

pw = driver.find_element(By.NAME, "password")
pw.send_keys(input_pw)

sleep(3)
# driver.find_element(By.CSS_SELECTOR, "#loginForm > div > div:nth-child(3)").click()
driver.find_element(By.XPATH, "/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]").click()