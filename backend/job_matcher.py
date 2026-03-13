jobs_db = [
    {
        "title": "Python Developer",
        "company": "TCS",
        "skills": ["python", "sql", "fastapi"]
    },
    {
        "title": "Data Analyst",
        "company": "Accenture",
        "skills": ["python", "sql", "excel"]
    },
    {
        "title": "Frontend Developer",
        "company": "Infosys",
        "skills": ["javascript", "html", "css", "react"]
    }
]


def match_jobs(user_skills):

    matched_jobs = []

    for job in jobs_db:

        job_skills = job["skills"]

        match_count = len(set(user_skills) & set(job_skills))

        match_percent = int((match_count / len(job_skills)) * 100)

        if match_percent > 0:

            matched_jobs.append({
                "title": job["title"],
                "company": job["company"],
                "match": f"{match_percent}%"
            })

    return matched_jobs
