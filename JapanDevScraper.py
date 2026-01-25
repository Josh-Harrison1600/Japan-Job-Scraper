import requests
from bs4 import BeautifulSoup
import time
import json
import JapanDevSettings

japan_dev_url = "https://japan-dev.com/jobs"
api_url = "https://meili.japan-dev.com/multi-search"
page = requests.get(japan_dev_url)
soup = BeautifulSoup(page.content, "html.parser")

job_posting_count = 0
compatiable_jobs = []
compatiable_jobs_count = 0
pages_to_scrape = 2
filename = "JapanDevJobs.json"


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
        
def _check_visa_sponsorship(sponsorship_value):
    if sponsorship_value == "sponsors_visas_yes":
        return "Yes"
    elif sponsorship_value == "sponsors_visas_no":
        return "No"
    return "Unknown"

def _check_candidate_location(location_value):
    if location_value == "candidate_location_japan_only":
        return "Japan Only"
    elif location_value == "candidate_location_anywhere":
        return "Anywhere"
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
    payload = JapanDevSettings._main_payload(current_offset)
    response = requests.post(api_url, json=payload, headers=JapanDevSettings.HEADERS)
    
    #200 = ok
    if response.status_code == 200:
        data = response.json()
        jobs = data['results'][0]['hits']
        
        #break if at the end of job postings
        if not jobs:
            break
        
        for job in jobs:
            
            #Define the variables that are used in the JSON call on the site
            lang = job.get("japanese_level_enum")
            level = job.get("seniority_level")
            title = job.get("title")
            visa = job.get("sponsors_visas")
            location = job.get("candidate_location")
            startup = job.get("company_is_startup")
            
            if (lang in JapanDevSettings.TOLERABLE_LANGUAGE_LEVEL) and (level in JapanDevSettings.TOLERABLE_EXPERIENCE_LEVEL):
                
                formatted_language = _check_language_level(lang)
                formatted_level = _check_seniority_level(level)
                will_sponsor = _check_visa_sponsorship(visa)
                can_apply = _check_candidate_location(location)
                
                #Only add to compatability list if they offer sponsorship
                if will_sponsor == "No":
                    continue
                
                ##Only add to compatability list if location is anywhere
                if can_apply == "Japan Only":
                    continue    
                
                
                is_startup = _startup_status(startup)
                job_url = _get_job_links(job)
                    
                job_info = f"Title: {title:<70} Level: {formatted_level:<30} Language: {formatted_language:<30} Startup: {is_startup:<10} URL: {job_url:<100}"
                job_entry = {"Title": title, "Level": level, "Language": lang, "URL": job_url}
                compatiable_jobs.append(job_entry)
                compatiable_jobs_count += 1
            
            print(" ")
            print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print("Job Title:         ", job['title'])
            print("Sponsors Visas?    ", job["sponsors_visas"])
            print("Application URL:   ", job["application_url"])
            print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print(" ")
            job_posting_count += 1
        time.sleep(1)
    else:
        print("failed to get data: ", response.status_code)
        print(response.text)
        break

#Store the results in json
try:
    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(compatiable_jobs, file, indent=4)
        print(f"Saved results to {filename}")
except IOError as e:
    print(f"Error writing to {filename}: {e}")

print("-----------------RESULTS-----------------")
print("Total Job Postings: ", job_posting_count)
print("Total Compatiable Jobs Found: ", compatiable_jobs_count)
print("-----------------------------------------")
