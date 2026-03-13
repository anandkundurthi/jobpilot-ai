# JobPilot AI

JobPilot AI is a smart job search assistant that helps users find relevant jobs using AI-based resume skill extraction.

##  Features

- Resume upload
- Skill extraction from resume
- Job matching based on skills
- Live job scraping
- Save jobs dashboard
- User login system
- FastAPI backend

##  Tech Stack

Backend:
- Python
- FastAPI
- BeautifulSoup
- Requests

Frontend:
- HTML
- CSS
- JavaScript

##  Project Structure

jobpilot-ai
│
├── backend
│   ├── main.py
│   ├── auth.py
│   ├── job_scraper.py
│   ├── skill_extractor.py
│
├── frontend
│   ├── index.html
│   ├── dashboard.html
│
└── README.md

## How to Run

Clone repository:

git clone https://github.com/anandkundurthi/jobpilot-ai.git

Go to backend:

cd backend

Install dependencies:

pip install fastapi uvicorn requests beautifulsoup4 pdfplumber passlib bcrypt

Run server:

uvicorn main:app --reload

Open frontend:

frontend/index.html

##  Demo

Upload resume → click **Find Jobs** → see matching jobs.

##  Author

Anand Kundurthi
