import requests
from bs4 import BeautifulSoup

japanDevUrl = "https://japan-dev.com/jobs"
page = requests.get(japanDevUrl)

soup = BeautifulSoup(page.content, "html.parser")

jobTitles = soup.find_all("div", class_="job-item__title-box")

for jobTitle in jobTitles:
    title = jobTitle.find("a", class_="job-item__title")
    print(title.text)