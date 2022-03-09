import time;
from selenium import webdriver;

#time to refresh page (seconds)
# Timer = 120

#youtube link
link = 'https://youtu.be/AjHay4FMaro'

#number of views
views = 100

driver = webdriver.Firefox()
driver.get(link)

for i in range(views):
    time.sleep(120)
    driver.refresh()
    print(i)