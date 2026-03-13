import pdfplumber

skills_db = [
    "python","java","sql","javascript",
    "html","css","react","node",
    "fastapi","django","flask",
    "machine learning","data analysis",
    "aws","docker","kubernetes"
]

def extract_skills(file_path):

    text = ""

    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text.lower()

    found_skills = []

    for skill in skills_db:
        if skill in text:
            found_skills.append(skill)

    return found_skills
