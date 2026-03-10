skills_list = [
"python",
"machine learning",
"deep learning",
"java",
"spring boot",
"tensorflow",
"sql",
"data science",
"nlp",
"react",
"node.js"
]

def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in skills_list:
        if skill in text:
            found_skills.append(skill)

    return found_skills