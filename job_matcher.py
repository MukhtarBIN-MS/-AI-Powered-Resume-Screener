from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import joblib
import os
from config import config
from logger import log_info, log_error

def load_models():
    """Load pre-trained models if available."""
    try:
        if os.path.exists(config.VECTOR_MODEL) and os.path.exists(config.CLASSIFIER_MODEL):
            vectorizer = joblib.load(config.VECTOR_MODEL)
            model = joblib.load(config.CLASSIFIER_MODEL)
        else:
            vectorizer = TfidfVectorizer()
            model = None  # No classifier for now

        log_info("Models loaded successfully.")
        return vectorizer, model
    except Exception as e:
        log_error(f"Error loading models: {str(e)}")
        return None, None

vectorizer, model = load_models()

def match_resume_with_job(resume_data, job_description):
    """Compare resume data with job description using TF-IDF similarity."""
    try:
        resume_text = " ".join(resume_data["skills"]) + " " + " ".join(resume_data["education"])
        texts = [resume_text, job_description]

        tfidf_matrix = vectorizer.fit_transform(texts)
        similarity_score = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])
        
        log_info(f"Resume match score: {similarity_score[0][0] * 100:.2f}%")
        return similarity_score[0][0] * 100
    except Exception as e:
        log_error(f"Error matching resume: {str(e)}")
        return 0
