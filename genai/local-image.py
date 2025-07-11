import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load environment variables from .env file
load_dotenv()

client = genai.Client()

# Use a raw string for the Windows file path
image_path = (
    r"C:\Users\sange\Downloads\1752115090647-787ac6a1-8971-496f-892d-021e62c9852f.png"
)

# Read the image as bytes
with open(image_path, "rb") as f:
    image_bytes = f.read()

# Use the correct mime type for your image
image_part = types.Part.from_bytes(
    data=image_bytes,
    mime_type="image/png",  # Change to "image/jpeg" if your image is JPEG
)

# Compose the prompt and image
contents = [
    image_part,
    "Describe this image in detail in JSON format with artstyle and artwork.",
]

# Call the model (Gemini 2.5 Flash, or use Pro for higher quality)
response = client.models.generate_content(model="gemini-2.5-flash", contents=contents)

print(response.text)
