import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests


ser = Service('D:/Learning/BeutifulSoupAndSelenium/chromedriver.exe')

driver = webdriver.Chrome(service=ser)
driver.get('http://www.google.com/')

search = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')

search.send_keys('dog')
search.send_keys(Keys.RETURN)

btn = driver.find_element(By.XPATH,'//*[@id="hdtb-msb"]/div[1]/div/div[2]/a')

btn.click()

url = driver.current_url

html = requests.get(url).text

soup = BeautifulSoup(html,'lxml')

gets = soup.find_all('h3', class_ = 'bytUYc')

print(gets)

for p in gets:
    pass



