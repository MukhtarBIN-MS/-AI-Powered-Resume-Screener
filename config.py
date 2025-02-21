import os

# Configuration for the application
class Config:
    DEBUG = True
    MODEL_PATH = "models/"
    VECTOR_MODEL = os.path.join(MODEL_PATH, "vectorizer.pkl")
    CLASSIFIER_MODEL = os.path.join(MODEL_PATH, "classifier.pkl")

config = Config()
