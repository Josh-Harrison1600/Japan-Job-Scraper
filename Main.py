from scrapers.JapanDevScraper import japan_dev_scraper
from scrapers.TokyoDevScraper import tokyo_dev_scraper
from SendEmail import send_email

japan_dev_jobs = japan_dev_scraper()
tokyo_dev_jobs = tokyo_dev_scraper()

send_email(japan_dev_jobs, tokyo_dev_jobs)