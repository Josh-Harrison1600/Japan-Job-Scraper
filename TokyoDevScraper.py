import requests
from bs4 import BeautifulSoup

HOME_URL = "https://www.tokyodev.com"
JOBS_URL = "https://www.tokyodev.com/jobs"
page = requests.get(JOBS_URL)

company_count = 0

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
    
def url_safety_check(element, URL):
    if element:
        print(URL + element['href'])
    elif not element:
        print("No url found for this job")
        
# List through the job names
for job_info in root_job_element.find_all("li"):
    
    company_name = job_info.find("a", class_="hover:text-indigo-600 dark:hover:text-indigo-400")
    safety_check(company_name, "company title")

    print('\n')
    for i in job_info.find_all("div", class_="relative first:mt-0 mt-4", attrs={"data-collapsable-list-target": "item"}):
        
        job_title = i.find("h4", class_="text-lg font-bold mb-1")
        safety_check(job_title, "job title")
        
        job_url = i.find("a", class_="font-bold hover:text-indigo-600 dark:hover:text-indigo-400", href=True)
        url_safety_check(job_url, HOME_URL)
        
        salary_data = i.find("a", class_="text-sm tag tag-primary")
        safety_check(salary_data, "salary data")

        no_japanese_required = i.find("a", href="/jobs/no-japanese-required")
        safety_check_no_output(no_japanese_required)
            
        japanese_required = i.find("a", href="/jobs/japanese-required")
        safety_check_no_output(japanese_required)
        
        apply_abroad = i.find("a", href="/jobs/apply-from-abroad") 
        safety_check_no_output(apply_abroad)
        
        japan_only = i.find("a", href="/jobs/residents-only")
        safety_check_no_output(japan_only)
        
        full_remote = i.find("a", href="/jobs/fully-remote")
        safety_check_no_output(full_remote)
        
        partially_remote = i.find("a", href="/jobs/partially-remote")
        safety_check_no_output(partially_remote)

        no_remote = i.find("a", href="/jobs/no-remote")
        safety_check_no_output(no_remote)
        print('\n')

    
    # Get all the job links from the company
    print('\n'"Job postings for this company:")
    for j in job_info.find_all("a", class_="font-bold hover:text-indigo-600 dark:hover:text-indigo-400", href=True):    
        print("    ", HOME_URL + j['href'])
    

    company_count += 1
    print(" ")
    print("---------------------- Company ", company_count, "----------------------")
    print(" ")
    
print("counted ", company_count, " companies")