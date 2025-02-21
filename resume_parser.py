import spacy
from utils import clean_text
from logger import log_info, log_error

# Load the NLP model
try:
    nlp = spacy.load("en_core_web_sm")
except Exception as e:
    log_error(f"Error loading NLP model: {str(e)}")
    raise e

def extract_resume_data(resume_text):
    """Extract key details from a resume using NLP."""
    try:
        cleaned_text = clean_text(resume_text)
        doc = nlp(cleaned_text)

        skills = [ent.text for ent in doc.ents if ent.label_ == "ORG"]
        education = [ent.text for ent in doc.ents if ent.label_ == "EDUCATION"]
        experience = [ent.text for ent in doc.ents if "year" in ent.text or "month" in ent.text]

        parsed_data = {
            "skills": list(set(skills)),
            "education": list(set(education)),
            "experience": experience
        }

        log_info(f"Resume parsed successfully: {parsed_data}")
        return parsed_data

    except Exception as e:
        log_error(f"Error parsing resume: {str(e)}")
        return {"error": "Failed to process resume"}
