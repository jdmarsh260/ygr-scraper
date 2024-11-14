import re
import csv
import time
import os
from bs4 import BeautifulSoup
from selenium import webdriver

#ask for URL
ygr_url = input("Enter the url for Yellow Green Red: ")

#opens browser and extracts html as soup text
url = ygr_url
browser = webdriver.Chrome()
browser.get(url)
time.sleep(5)
html = browser.page_source
soup = BeautifulSoup(html, 'html.parser')

with open('ygr.txt', 'w', encoding='utf8') as file:
	file.write(str(soup))
file.close()

with open("ygr.txt", 'r', encoding='utf8') as html_file:
	soup = BeautifulSoup(html_file, 'lxml')


with open('ygr.csv', 'a', encoding='utf8') as csv_file:
    csv_writer = csv.writer(csv_file)

    for title in soup.find_all('p'):
        paragraphs = title.text
        edited_headlines = []
        i = 0

        headline = paragraphs.split('<br/>')
        headline = paragraphs.splitlines()[0]
        headline = re.sub(r'(?:7″|12″|7"|12"|LP|EP|compilation|Compilation)',' ', headline)
        edited_headlines.append(headline)
        while i <len(edited_headlines):
            edited_headlines_final = re.sub(r'\(.*?\)', ' ', edited_headlines[i])
            print(edited_headlines_final)
            csv_writer.writerow([edited_headlines_final])
            i += 1

os.remove(('ygr.txt'))