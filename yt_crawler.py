from selenium import webdriver
from selenium.webdriver.common.by import By

path_to_chromedriver = 'chromedriver/chromedriver'
browser = webdriver.Chrome(executable_path = path_to_chromedriver)

url = 'https://www.youtube.com/results?search_query=chitaozinho+e+xororo'
browser.get(url)

filename = "chitaozinhoexororo.csv"
f = open(filename, "w")

headers = "title, views\n"
f.write(headers)

titles = browser.find_elements(By.CSS_SELECTOR, '#contents > ytd-video-renderer > #dismissable > div > #meta > #title-wrapper > h3 > #video-title')
views = browser.find_elements(By.CSS_SELECTOR, '#contents > ytd-video-renderer > #dismissable > div > #meta > ytd-video-meta-block > #metadata > #metadata-line > span:nth-child(1)')

num_videos = len(titles)

for i in range(num_videos):
	print(titles[i].text +': '+views[i].text)

	f.write(titles[i].text + "," + views[i].text + "\n")

browser.close()
f.close()

