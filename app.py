import streamlit as st
from resume_parser import extract_text
from skills_extractor import extract_skills
from question_generator import generate_questions

st.title("InterviewAI – AI Interview Preparation Assistant")

uploaded_file = st.file_uploader("Upload your resume", type="pdf")

if uploaded_file:

    text = extract_text(uploaded_file)

    st.success("Resume uploaded successfully!")

    skills = extract_skills(text)

    st.write("Detected Skills:", skills)

    if st.button("Generate Interview Questions"):

        questions = generate_questions(skills)

        st.write(questions)
