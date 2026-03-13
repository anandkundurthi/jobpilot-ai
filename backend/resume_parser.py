from pdfminer.high_level import extract_text

skills = [
    "python",
    "sql",
    "react",
    "fastapi",
    "node",
    "docker",
    "aws"
]

def extract_skills(file_path):

    text = extract_text(file_path)

    found_skills = []

    for skill in skills:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    return found_skills
