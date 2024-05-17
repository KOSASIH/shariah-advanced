# config.py

# API Configurations
OPENAI_API_KEY = 'your_openai_api_key_here'
OLLAMA_API_KEY = 'your_ollama_api_key_here'
API_URL = "https://localhost:11434"
HEADERS = {'Content-Type': 'application/json'}
MODEL = 'llama3'  # Options: 'gpt-3', 'gpt-4', 'llama3'

# New configurations moved from main.py
RETRY_TIMES = 3
BACKOFF_FACTOR = 0.3
TIMEOUT = 60

# Document Configurations
SUBTITLE = 'Made by AI Expert Agents'
PROMPTS_FILE = 'prompts.json'
LOG_FILE = 'last_project.log'

# General Instructions for AI to maintain context and avoid repetition
GENERAL_INSTRUCTIONS = (
    "In generating content for each section, maintain coherence with the overall context "
    "of the project '{project_name}', described as '{project_description}'. Avoid repetitive "
    "information across sections and focus on providing unique, relevant insights in each part. "
    "Ensure that the content is investor-focused and aligns with the main objective of presenting "
    "a comprehensive feasibility study."
)
