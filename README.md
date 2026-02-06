# Japan Job Scraper

### Japan Job Scraper is a Python scraper I built to scrape two popular software engineering job boards in Japan, <a href="https://www.tokyodev.com/" target=_blank>TokyoDev</a> and  <a href="https://japan-dev.com/" target=_blank>JapanDev</a>.
### The scraper uses GitHub Actions and cron to run once a day to detect new jobs that have been posted which it will then email me the results.

# Setting up the Scraper

### To use this scrpaer yourself follow the instructions below:

- Clone the repo
- Create the enviornment by running ````python -m venv venv````
- Activate the environment ````.\venv\Scripts\activate````
- Change the email address in SendMail.py
- Configure your own <a href="https://support.google.com/mail/answer/185833?hl=en">App Password</a>
- Run the scraper ````Python .\Main.py````
