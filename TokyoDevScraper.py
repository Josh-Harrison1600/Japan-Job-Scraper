import requests
from bs4 import BeautifulSoup

URL = "https://www.tokyodev.com/jobs"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
titles = soup.find_all("a", class_="hover:text-indigo-600 dark:hover:text-indigo-400")

# Format the output
for job_title in titles:
    print(job_title.prettify())
    print(" ")
    print("---")
    print(" ")