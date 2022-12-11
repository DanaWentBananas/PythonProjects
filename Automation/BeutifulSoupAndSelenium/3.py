from bs4 import BeautifulSoup
import requests

url = 'https://www.google.com/search?q=dog&source=lnms&tbm=isch&sa=X&ved=2ahUKEwi5tPz42-P3AhUyiv0HHS8fDyUQ_AUoAXoECAIQAw&biw=1036&bih=666&dpr=1.25'

html = requests.get(url).text

soup = BeautifulSoup(html,'lxml')

gets = soup.find_all('h3', class_ = 'bytUYc')

print(gets)
