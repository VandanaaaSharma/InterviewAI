import spacy

nlp = spacy.load("en_core_web_sm")

skills_list = [
"python",
"machine learning",
"deep learning",
"java",
"spring boot",
"tensorflow",
"sql",
"data science",
"nlp"
]

def extract_skills(text):

    doc = nlp(text.lower())

    found_skills = []

    for skill in skills_list:
        if skill in text.lower():
            found_skills.append(skill)

    return found_skills
