import requests
from bs4 import BeautifulSoup
import datetime
import re
from config.settings import BASE_URL, USER_AGENT

def scrape_jobs():
    headers = {"User-Agent": USER_AGENT}
    response = requests.get(BASE_URL, headers=headers)
    if response.status_code != 200:
        print(f"[ERROR] Failed to fetch page: {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    job_cards = soup.find_all("div", class_="styles_roleListing__roleListingCard__Q6BtG")

    jobs = []
    for job in job_cards:
        title = job.find("h2")
        company = job.find("h3")
        location = job.find("span", class_="styles_jobLocation__ZszZ5")
        salary = job.find("span", string=re.compile(r"\$"))

        jobs.append({
            "title": title.get_text(strip=True) if title else None,
            "company": company.get_text(strip=True) if company else None,
            "location": location.get_text(strip=True) if location else None,
            "salary": salary.get_text(strip=True) if salary else None,
            "date_scraped": datetime.date.today()
        })

    return jobs
