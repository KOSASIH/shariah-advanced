import re

def preprocess_text(text):
    text = re.sub(r'[^\w\s]', '', text)
    return text
