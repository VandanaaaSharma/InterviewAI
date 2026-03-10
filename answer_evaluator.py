import google.generativeai as genai

genai.configure(api_key="AIzaSyAPvODV8GF_7dSIGB9ehVPQ7ntZXX82xyQ")

model = genai.GenerativeModel("gemini-pro")

def evaluate_answer(question, answer):

    prompt = f"""
    Question: {question}
    Answer: {answer}

    Evaluate this answer.
    Give score out of 10 and feedback.
    """

    response = model.generate_content(prompt)

    return response.text
