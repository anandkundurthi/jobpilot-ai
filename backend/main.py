from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os

from skill_extractor import extract_skills
from job_scraper import scrape_jobs
from auth import create_user, authenticate_user

app = FastAPI()

# Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_FOLDER = "resumes"

# create resumes folder
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# simple in-memory storage
saved_jobs = []


# -------------------------
# USER AUTHENTICATION
# -------------------------

@app.post("/signup")
async def signup(username: str, password: str):

    create_user(username, password)

    return {"message": "User created successfully"}


@app.post("/login")
async def login(username: str, password: str):

    if authenticate_user(username, password):
        return {"message": "Login successful"}

    return {"message": "Invalid credentials"}


# -------------------------
# MATCH JOBS
# -------------------------

@app.post("/match-jobs")
async def match_jobs(file: UploadFile = File(...)):

    file_path = f"{UPLOAD_FOLDER}/{file.filename}"

    # save uploaded resume
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # extract skills
    skills = extract_skills(file_path)

    jobs = []

    # scrape jobs using first detected skill
    if skills:
        jobs = scrape_jobs(skills[0])

    return {
        "skills": skills,
        "jobs": jobs
    }


# -------------------------
# SAVE JOB
# -------------------------

@app.post("/save-job")
async def save_job(job: dict):

    saved_jobs.append(job)

    return {"message": "Job saved successfully"}


# -------------------------
# GET SAVED JOBS
# -------------------------

@app.get("/saved-jobs")
async def get_saved_jobs():

    return {
        "jobs": saved_jobs
    }
