from utils import *
from selenium import webdriver
from bs4 import BeautifulSoup
import time

# from selenium.webdriver.chrome.service import Service

# Если chrome отстутствует
# https://sites.google.com/chromium.org/driver/
# Необходимо выдать права на исполнение chromedriver !!!
# service = Service(executable_path='./chromedriver')
# options = webdriver.ChromeOptions()
# driver = webdriver.Chrome(service=service, options=options)

driver = webdriver.Chrome(executable_path="chromedriver")

YT_LINK = 'https://www.youtube.com/@MrBeast'
VK_LINK = 'https://vk.com/nrnews24'


# YouTube

driver.get(YT_LINK)

time.sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

source = driver.page_source
html = BeautifulSoup(source, 'html.parser')

subscriber_count_element = html.find('yt-formatted-string', {'id': 'subscriber-count'})
subscribers_count_yt = 0
try: 
  subscribers_count_yt = convert_subscribers_count(subscriber_count_element.text.strip())
except: 
  pass  


# VK

driver.get(VK_LINK)

time.sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

source = driver.page_source
html = BeautifulSoup(source, 'html.parser')

subscriber_count_element = html.find('span', {"class": "header_count"})
subscribers_count_vk = 0
try:
  subscribers_count_vk = int(subscriber_count_element.text.strip().replace(' ', ''))
except: 
  pass


print(f"YT: {subscribers_count_yt}")
print(f"VK: {subscribers_count_vk}")

driver.quit()