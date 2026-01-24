import requests
from bs4 import BeautifulSoup
import time

japan_dev_url = "https://japan-dev.com/jobs"
api_url = "https://meili.japan-dev.com/multi-search"
page = requests.get(japan_dev_url)
soup = BeautifulSoup(page.content, "html.parser")

job_posting_count = 0
compatiable_jobs = []
compatiable_jobs_count = 0
pages_to_scrape = 2

tolerable_language_level = [
    "japanese_level_not_required",
    "japanese_level_conversational"
]

tolerable_experience_level = [
    "seniority_level_junior",
    "seniority_level_mid_level"
]

visa_sponsorship = "sponsors_visas_yes"

headers = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Authorization": "Bearer 3838486cea4344beaef2c4c5979be249fc5736ea4aab99fab193b5e7f540ffae",
    "X-Meilisearch-Client": "Meilisearch instant-meilisearch (v0.20.1) ; Meilisearch JavaScript (v0.42.0)"
}

def _check_seniority_level(level_value):
    if level_value == "seniority_level_junior":
        return "Junior"
    elif level_value == "seniority_level_mid_level":
        return"Intermediate"
    return "Unknown"
        
def _check_language_level(language_value):
    if language_value == "japanese_level_not_required":
        return "No Japanese"
    elif language_value == "japanese_level_conversational":
        return "Conversational Japanese"
    return "Unknown"
        
def _startup_status(startup_status):
    if startup_status is False:
        return "No"
    elif startup_status is True:
        return "Yes"
    return "Unknown"
        
def _get_job_links(job_data):
    formatted_info = job_data.get("_formatted", {})
    formatted_slug = formatted_info.get("slug")
    
    company_info = formatted_info.get("company", {})
    company_slug = company_info.get("slug")
    
    if formatted_info and company_info: 
        return f"https://japan-dev.com/jobs/{company_slug}/{formatted_slug}"
    
    return "No Link"
    
    
for page_number in range(pages_to_scrape):
    current_offset = page_number * 21
    
    payload = {
        "queries": [
            {
                "indexUid": "Job_production",
                "q": "",
                "limit": 21,
                "offset": current_offset,
                "facets": ["location", "job_type_names"],
                "attributesToHighlight":["*"]
            }
        ]
    }
    
    response = requests.post(api_url, json=payload, headers=headers)
    
    #200 = ok
    if response.status_code == 200:
        data = response.json()
        jobs = data['results'][0]['hits']
        
        #break if at the end of job postings
        if not jobs:
            break
        
        for job in jobs:
            
            lang = job.get("japanese_level_enum")
            level = job.get("seniority_level")
            title = job.get("title")
            startup = job.get("company_is_startup")
            
            if (lang in tolerable_language_level) and (level in tolerable_experience_level):
                
                formatted_language = _check_language_level(lang)
                formatted_level = _check_seniority_level(level)
                is_startup = _startup_status(startup)
                job_url = _get_job_links(job)
                    
                job_info = f"Title: {title:<70} Level: {formatted_level:<30} Language: {formatted_language:<30} Startup: {is_startup:<10} URL: {job_url}"
                compatiable_jobs.append(job_info)
                compatiable_jobs_count += 1
            
            
            array_output = "\n".join((compatiable_jobs))
            
            print(" ")
            print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print("Job Title:         ", job['title'])
            print("Sponsors Visas?    ", job["sponsors_visas"])
            print("Application URL:   ", job["application_url"])
            print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print(" ")
            job_posting_count += 1
        time.sleep(1)
    else:
        print("failed to get data: ", response.status_code)
        print(response.text)
        break


print("----------------------------------")
print("Total Job Postings: ", job_posting_count)
print("----------------------------------")


print("----------------------------------")
print("Total Compatiable Jobs Found: ", compatiable_jobs_count)
print(" ")
print(array_output)
print("----------------------------------")