import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

# The Client will read GEMINI_API_KEY from the environment
client = genai.Client()

stream = client.models.generate_content_stream(
    model="gemini-2.5-flash-lite-preview-06-17",
    contents="Summarize the latest advancements in AI.",
)

 
for chunk in stream:
    print(chunk.text, end="", flush=True)
print()  
