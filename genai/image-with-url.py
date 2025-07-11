import os
import sys

import requests
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load environment variables from .env file
load_dotenv()

client = genai.Client()

# Get image URL from command-line argument
if len(sys.argv) < 2:
    print("Usage: python image_url_analysis.py <IMAGE_URL>")
    sys.exit(1)

image_url = sys.argv[1]

# Download the image from the URL
response = requests.get(image_url)
response.raise_for_status()
image_bytes = response.content

# Guess the mime type from the URL extension (simple version)
if image_url.lower().endswith(".png"):
    mime_type = "image/png"
elif image_url.lower().endswith((".jpg", ".jpeg")):
    mime_type = "image/jpeg"
else:
    mime_type = "application/octet-stream"  # fallback

image_part = types.Part.from_bytes(data=image_bytes, mime_type=mime_type)

contents = [
    image_part,
    "Describe this image in detail in JSON format with artstyle and artwork.",
]

response = client.models.generate_content(model="gemini-2.5-flash", contents=contents)

print(response.text)
