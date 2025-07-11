import os

from dotenv import load_dotenv
from google import genai

# Load environment variables from .env file
load_dotenv()

# The Client will read GEMINI_API_KEY from the environment
client = genai.Client()

# Use the streaming method
stream = client.models.generate_content_stream(
    model="gemini-2.5-flash-lite-preview-06-17",
    contents="Summarize the latest advancements in AI.",
)

# Print the streamed response as it arrives
for chunk in stream:
    print(chunk.text, end="", flush=True)
print()  # for a final newline
