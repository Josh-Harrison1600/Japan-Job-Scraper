import requests
from bs4 import BeautifulSoup

HOME_URL = "https://www.tokyodev.com"
JOBS_URL = "https://www.tokyodev.com/jobs"
page = requests.get(JOBS_URL)

job_posting_count = 0

soup = BeautifulSoup(page.content, "html.parser")
root_job_element = soup.find("ul", class_="relative list-inside")

def safety_check(element, output):
    if element:
        print(element.text)
    elif not element:
        print("No ", output, " for this posting")
    
def safety_check_no_output(element):
    if element:
        print(element.text)
    elif not element:
        return
        
# List through the job names
for job_info in root_job_element.find_all("li"):
    
    job_title = job_info.find("a", class_="hover:text-indigo-600 dark:hover:text-indigo-400")
    safety_check(job_title, "job title")

        
    salary_data = job_info.find("a", class_="text-sm tag tag-primary")
    safety_check(salary_data, "salary data")

    
    no_japanese_required = job_info.find("a", href="/jobs/no-japanese-required")
    safety_check_no_output(no_japanese_required)
        
    japanese_required = job_info.find("a", href="/jobs/japanese-required")
    safety_check_no_output(japanese_required)
    
    apply_abroad = job_info.find("a", href="/jobs/apply-from-abroad") 
    safety_check_no_output(apply_abroad)
    
    japan_only = job_info.find("a", href="/jobs/residents-only")
    safety_check_no_output(japan_only)
    
    full_remote = job_info.find("a", href="/jobs/fully-remote")
    safety_check_no_output(full_remote)
    
    partially_remote = job_info.find("a", href="/jobs/partially-remote")
    safety_check_no_output(partially_remote)

    no_remote = job_info.find("a", href="/jobs/no-remote")
    safety_check_no_output(no_remote)
    
    print('\n'"Job postings for this company:")
    for i in job_info.find_all("a", class_="font-bold hover:text-indigo-600 dark:hover:text-indigo-400", href=True):    
        print("    ", HOME_URL + i['href'])
    

    job_posting_count += 1
    print(" ")
    print("---------------------- Job ", job_posting_count, "----------------------")
    print(" ")
    
print("counted ", job_posting_count, " jobs")