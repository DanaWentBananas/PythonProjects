from bs4 import BeautifulSoup
import requests

html = requests.get('https://ae.indeed.com/jobs?q=python&l=Dubai&vjk=81dd8175ac714a46').text

soup = BeautifulSoup(html,'lxml')

jobs = soup.find_all('h2', class_ = 'jobTitle')

for t in jobs:
    print(t.find('a').find('span').text)
    
