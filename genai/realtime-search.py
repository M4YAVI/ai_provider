import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

client = genai.Client()

# Create the Tool object for Google Search grounding
search_tool = types.Tool(google_search=types.GoogleSearch())

# Use the streaming method with the config parameter
stream = client.models.generate_content_stream(
    model="gemini-2.5-flash-lite-preview-06-17",
    contents="Summarize today's top AI news headlines with sources.",
    config=types.GenerateContentConfig(tools=[search_tool]),
)

for chunk in stream:
    print(chunk.text, end="", flush=True)
print()
