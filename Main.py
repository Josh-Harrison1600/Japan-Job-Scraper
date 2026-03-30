from scrapers.JapanDevScraper import japan_dev_scraper
from scrapers.TokyoDevScraper import tokyo_dev_scraper
from emailer.SendEmail import send_email

def main():
    try:
        print("Starting Japan Dev Scraper...")
        japan_dev_jobs = japan_dev_scraper()
        
        print("Starting Tokyo Dev Scraper...")
        tokyo_dev_jobs = tokyo_dev_scraper()
        
        print("Sending email...")
        send_email(japan_dev_jobs, tokyo_dev_jobs)
        
        print("Workflow completed successfully.")
    except Exception as e:
        print(f"ERROR: The script failed due to: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
