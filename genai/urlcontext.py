import os

from dotenv import load_dotenv
from google import genai
from google.genai.types import GenerateContentConfig, Tool, UrlContext

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("GOOGLE_API_KEY not found in environment variables.")

# Initialize the Gemini client with the API key
client = genai.Client(api_key=api_key)

# Define the URLs to compare (real recipe pages)
url1 = "https://www.allrecipes.com/recipe/24074/alysias-basic-meat-lasagna/"
url2 = "https://www.simplyrecipes.com/recipes/lasagna/"

# Create the URL context tool
url_context_tool = Tool(url_context=UrlContext())

# Compose your prompt
prompt = (
    f"Compare recipes from {url1} and {url2}. "
    "Highlight differences in ingredients, preparation steps, and cooking time."
)

# Generate content using Gemini with URL context
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt,
    config=GenerateContentConfig(
        tools=[url_context_tool],
        response_modalities=["TEXT"],
    ),
)

# Print the response text from all candidates
for candidate in response.candidates:
    for part in candidate.content.parts:
        print(part.text)

# Optionally, print metadata about which URLs were processed
if hasattr(response.candidates[0], "url_context_metadata"):
    print(response.candidates[0].url_context_metadata)
