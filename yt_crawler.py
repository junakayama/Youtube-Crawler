from selenium import webdriver
from selenium.webdriver.common.by import By

path_to_chromedriver = 'chromedriver/chromedriver'
browser = webdriver.Chrome(executable_path = path_to_chromedriver)

url = 'https://www.youtube.com/results?search_query=chitaozinho+e+xororo'
browser.get(url)

titles = browser.find_elements(By.CSS_SELECTOR, '#contents > ytd-video-renderer > #dismissable > div > #meta > #title-wrapper > h3 > #video-title')
num_titles = len(titles)
for i in range(num_titles):
	print(titles[i].text)

browser.close()
