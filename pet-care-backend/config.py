import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve the OpenAI API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
