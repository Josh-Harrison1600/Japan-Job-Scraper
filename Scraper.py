import requests
from bs4 import BeautifulSoup
import time

japanDevUrl = "https://japan-dev.com/jobs"
apiUrl = "https://meili.japan-dev.com/multi-search"
page = requests.get(japanDevUrl)
soup = BeautifulSoup(page.content, "html.parser")

jobPostings = 0
japaneseOnly = 0
yesVisa = 0
noVisa = 0


headers = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Authorization": "Bearer 3838486cea4344beaef2c4c5979be249fc5736ea4aab99fab193b5e7f540ffae",
    "X-Meilisearch-Client": "Meilisearch instant-meilisearch (v0.20.1) ; Meilisearch JavaScript (v0.42.0)"
}

for page_number in range(99):
    current_offset = page_number * 21
    
    payload = {
        "queries": [
            {
                "indexUid": "Job_production",
                "q": "",
                "limit": 21,
                "offset": current_offset,
                "facets": ["location", "job_type_names"] 
            }
        ]
    }
    
    response = requests.post(apiUrl, json=payload, headers=headers)
    
    #200 = ok
    if response.status_code == 200:
        data = response.json()
        jobs = data['results'][0]['hits']
        
        #break if at the end of job postings
        if not jobs:
            print("No more jobs found")
            break
        
        for job in jobs:
            
            if(job["is_japanese_only"] == True):
                japaneseOnly += 1
            
            if(job["sponsors_visas"] == "sponsors_visas_yes"):
                yesVisa += 1
                
            if(job["sponsors_visas"] == "sponsors_visas_no"):
                noVisa += 1
            
            print(" ")
            print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print("Job Title:         ", job['title'])
            print("Sponsors Visas?    ", job["sponsors_visas"])
            print("Application URL:   ", job["application_url"])
            print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print(" ")
            jobPostings += 1
        time.sleep(1)
    else:
        print("failed to get data: ", response.status_code)
        print(response.text)
        break


print("----------------------------------")
print("total job postings: ", jobPostings)
print("Japanese only companies: ", japaneseOnly)
print("Companies offering visa: ", yesVisa)
print("Companies NOT offering visa: ", noVisa)
print("----------------------------------")
