import re

def clean_text(text):
    """Clean and normalize text."""
    text = re.sub(r"\s+", " ", text)  # Remove multiple spaces
    text = re.sub(r"[^\w\s]", "", text)  # Remove special characters
    return text.lower()
