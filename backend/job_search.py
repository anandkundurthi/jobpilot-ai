def search_jobs(skills):

    jobs_db = [
        {
            "title":"Python Developer",
            "company":"Google",
            "skills":["python","sql","docker"]
        },
        {
            "title":"Data Analyst",
            "company":"Amazon",
            "skills":["python","sql","excel"]
        },
        {
            "title":"Frontend Developer",
            "company":"Meta",
            "skills":["javascript","react","html","css"]
        },
        {
            "title":"Backend Developer",
            "company":"Microsoft",
            "skills":["python","fastapi","docker"]
        }
    ]

    matched_jobs = []

    for job in jobs_db:

        job_skills = job["skills"]

        match_count = len(set(skills) & set(job_skills))

        if match_count > 0:

            match_percent = int((match_count/len(job_skills))*100)

            matched_jobs.append({
                "title":job["title"],
                "company":job["company"],
                "match":f"{match_percent}%"
            })

    return matched_jobs
