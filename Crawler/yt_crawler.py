from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options

start = time.time()

# Simulating Chrome Browser
path_to_chromedriver = 'chromedriver/chromedriver'
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')  # Last I checked this was necessary.
browser = webdriver.Chrome(executable_path = path_to_chromedriver, chrome_options=options)


# Grabbing the page
browser.get('https://www.youtube.com/results?search_query=chitaozinho+e+xororo')

# Creating csv file
f = open("chitaozinhoexororo.csv", "w")
headers = "title, views\n"
f.write(headers)

# Finding the titles and views
titles = browser.find_elements(By.CSS_SELECTOR, '#contents > ytd-video-renderer > #dismissable > div > #meta > #title-wrapper > h3 > #video-title')
views = browser.find_elements(By.CSS_SELECTOR, '#contents > ytd-video-renderer > #dismissable > div > #meta > ytd-video-meta-block > #metadata > #metadata-line > span:nth-child(1)')
num_videos = len(titles)


# Writing the titles and views to csv file
for i in range(num_videos):
	print(titles[i].text +': '+views[i].text)
	f.write(titles[i].text + "," + views[i].text + "\n")

# Closing the browser and the file
browser.close()
f.close()

# Calculating execution time
end = time.time()
execution_time = str(end - start)
print("Execution time: "+ execution_time + " seconds")
