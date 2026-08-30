from dotenv import load_dotenv
from google import genai
import os
from pathlib import Path

# Find the .env file
project_folder = Path(__file__).resolve().parent.parent
env_file = project_folder / ".env"

load_dotenv(env_file)

# Get API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY was not found.")

print("API key loaded successfully!")

# Create Gemini client
client = genai.Client(api_key=api_key)

# Send a simple test request using the current Interactions API
interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Explain what a RAG chatbot is in one simple sentence."
)

print("\nGemini is working successfully!")
print("\nResponse:")
print(interaction.output_text)