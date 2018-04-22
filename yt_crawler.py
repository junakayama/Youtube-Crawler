from bs4 import BeautifulSoup as soup
import requests

r = requests.get('https://www.youtube.com/results?search_query=chitaozinho+e+xororo')
page_html = r.text

page_soup = soup(page_html, "html.parser")

