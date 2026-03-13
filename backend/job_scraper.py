import requests
from bs4 import BeautifulSoup
import urllib3

urllib3.disable_warnings()

def scrape_jobs(keyword):

    url = f"https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&txtKeywords={keyword}"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers, verify=False)

    soup = BeautifulSoup(response.text, "html.parser")

    jobs = []

    job_cards = soup.find_all("li", class_="clearfix job-bx wht-shd-bx")

    for job in job_cards[:5]:

        title = job.find("h2").text.strip()
        company = job.find("h3").text.strip()

        jobs.append({
            "title": title,
            "company": company,
            "match": "Live Job"
        })

    return jobs
