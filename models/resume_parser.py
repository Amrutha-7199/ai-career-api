import spacy
import re

nlp = spacy.load("en_core_web_sm")

def extract_skills(text):
    """Extracts skills using NLP techniques."""
    doc = nlp(text)
    skills = set(token.text.lower() for token in doc if token.pos_ in ["NOUN", "PROPN"])
    return list(skills)

def extract_experience(text):
    """Extracts work experience duration from resume."""
    experience = re.findall(r'(\d+)\s+years', text)
    total_experience = sum(map(int, experience)) if experience else 0
    return total_experience

def parse_resume(resume_text):
    """Extracts key information from resume."""
    skills = extract_skills(resume_text)
    experience = extract_experience(resume_text)
    return {"skills": skills, "experience": experience}
