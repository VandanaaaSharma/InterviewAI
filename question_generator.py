import google.generativeai as genai

genai.configure(api_key="AIzaSyAPvODV8GF_7dSIGB9ehVPQ7ntZXX82xyQ")

model = genai.GenerativeModel("gemini-1.5-flash")

def generate_questions(skills):

    prompt = f"""
    Generate 5 technical interview questions for these skills:
    {skills}
    """

    response = model.generate_content(prompt)

    return response.text
